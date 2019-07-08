import pygame
import random
import math

SCREEN_DIM = (800, 600)


class Polyline:
    @staticmethod
    def draw_points(points, style="points", width=3, color=(255, 255, 255)):
        if style == "line":
            for p_n in range(-1, len(points) - 1):
                pygame.draw.line(gameDisplay, color,
                                 points[p_n].int_pair(),
                                 points[p_n+1].int_pair(),
                                 width)

        elif style == "points":
            for p in points:
                pygame.draw.circle(gameDisplay, color,
                                   p.int_pair(), width)

    @staticmethod
    def set_points(points, speeds):
        for p in range(len(points)):
            points[p] = points[p] + speeds[p]
            if points[p][0] > SCREEN_DIM[0] or points[p][0] < 0:
                speeds[p] = (- speeds[p][0], speeds[p][1])
            if points[p][1] > SCREEN_DIM[1] or points[p][1] < 0:
                speeds[p] = (speeds[p][0], -speeds[p][1])

    # Сглаживание ломаной
    @staticmethod
    def get_point(points, alpha, deg=None):
        if deg is None:
            deg = len(points) - 1
        if deg == 0:
            return points[0]
        return (points[deg] * alpha) + \
            Polyline.get_point(points, alpha, deg - 1) * (1 - alpha)

    @staticmethod
    def get_points(base_points, count):
        alpha = 1 / count
        res = []
        for i in range(count):
            res.append(Polyline.get_point(base_points, i * alpha))
        return res


class Knot:
    @staticmethod
    def get_knot(points, count):
        if len(points) < 3:
            return []
        res = []
        for i in range(-2, len(points) - 2):
            ptn = []
            ptn.append((points[i]+points[i + 1])*0.5)
            ptn.append(points[i + 1])
            ptn.append((points[i + 1]+points[i + 2])*0.5)
            res.extend(Polyline.get_points(ptn, count))
        return res


class Vec2d:
    def __init__(self, point):
        self.point = point

    def __add__(self, other):
        return Vec2d((self.point[0] + other.point[0],
                      self.point[1] + other.point[1]))

    def __sub__(self, other):
        return Vec2d((self.point[0] - other.point[0],
                      self.point[1] - other.point[1]))

    def __mul__(self, other):
        if other is Vec2d:
            return self.point[0] * other.point[0] \
                   + self.point[1] * other.point[1]
        else:
            return Vec2d((self.point[0] * other,
                          self.point[1] * other))

    def __len__(self):
        return math.sqrt(self.point[0] * self.point[0]
                         + self.point[1] * self.point[1])

    def int_pair(self):
        return int(self.point[0]), int(self.point[1])


# Отрисовка справки
class Helper:
    @staticmethod
    def draw_help():
        gameDisplay.fill((50, 50, 50))
        font1 = pygame.font.SysFont("courier", 24)
        font2 = pygame.font.SysFont("serif", 24)
        data = []
        data.append(["F1", "Show Help"])
        data.append(["R", "Restart"])
        data.append(["P", "Pause/Play"])
        data.append(["Num+", "More points"])
        data.append(["Num-", "Less points"])
        data.append(["", ""])
        data.append([str(steps), "Current points"])

        pygame.draw.lines(gameDisplay, (255, 50, 50, 255), True, [
                      (0, 0), (800, 0), (800, 600), (0, 600)], 5)
        for i, text in enumerate(data):
            gameDisplay.blit(font1.render(
                text[0], True, (128, 128, 255)), (100, 100 + 30 * i))
            gameDisplay.blit(font2.render(
                text[1], True, (128, 128, 255)), (200, 100 + 30 * i))


# Основная программа
if __name__ == "__main__":
    pygame.init()
    gameDisplay = pygame.display.set_mode(SCREEN_DIM)
    pygame.display.set_caption("MyScreenSaver")

    steps = 35
    working = True
    points = []
    speeds = []
    show_help = False
    pause = True

    hue = 0
    color = pygame.Color(0)

    while working:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                working = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    working = False
                if event.key == pygame.K_r:
                    points = []
                    speeds = []
                if event.key == pygame.K_p:
                    pause = not pause
                if event.key == pygame.K_KP_PLUS:
                    steps += 1
                if event.key == pygame.K_F1:
                    show_help = not show_help
                if event.key == pygame.K_KP_MINUS:
                    steps -= 1 if steps > 1 else 0

            if event.type == pygame.MOUSEBUTTONDOWN:
                points.append(Vec2d(event.pos))
                speeds.append((random.random() * 2, random.random() * 2))

        gameDisplay.fill((0, 0, 0))
        hue = (hue + 1) % 360
        color.hsla = (hue, 100, 50, 100)
        Polyline.draw_points(points)
        Polyline.draw_points(Knot.get_knot(points, steps), "line", 3, color)
        if not pause:
            Polyline.set_points(points, speeds)
        if show_help:
            Helper.draw_help()

        pygame.display.flip()

    pygame.display.quit()
    pygame.quit()
    exit(0)
