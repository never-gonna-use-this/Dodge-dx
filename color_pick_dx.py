import colorsys

import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
BLACK = (20, 20, 41)
WHITE = (240, 240, 245)
GRAY = (70, 70, 100)
pygame.display.set_caption("Color Pick DX")
clock = pygame.time.Clock()

font = pygame.font.SysFont(None, 30)
small = pygame.font.SysFont(None, 24)


class Slider:
    """A horizontal slider that holds a value from 0 to 255."""

    def __init__(self, x, y, w, label, tint, value=128):
        self.x, self.y, self.w = x, y, w
        self.label = label
        self.tint = tint
        self.value = value
        self.dragging = False

    @property
    def knob_x(self):
        return self.x + int(self.value / 255 * self.w)

    def set_from_mouse(self, mouse_x):
        ratio = (mouse_x - self.x) / self.w
        self.value = round(max(0, min(1, ratio)) * 255)

    def handle(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            hit_area = pygame.Rect(self.x - 14, self.y - 16, self.w + 28, 32)
            if hit_area.collidepoint(event.pos):
                self.dragging = True
                self.set_from_mouse(event.pos[0])
        elif event.type == pygame.MOUSEMOTION and self.dragging:
            self.set_from_mouse(event.pos[0])
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            self.dragging = False

    def draw(self, surface):
        track = pygame.Rect(self.x, self.y - 5, self.w, 10)
        pygame.draw.rect(surface, GRAY, track, border_radius=5)
        filled = pygame.Rect(self.x, self.y - 5, self.knob_x - self.x, 10)
        pygame.draw.rect(surface, self.tint, filled, border_radius=5)
        pygame.draw.circle(surface, WHITE, (self.knob_x, self.y), 12)
        pygame.draw.circle(surface, self.tint, (self.knob_x, self.y), 8)
        text = font.render(f"{self.label}: {self.value}", True, WHITE)
        surface.blit(text, (self.x, self.y - 40))


def describe(r, g, b):
    """Return short lines that teach what the current color is made of."""
    if r == g == b:
        return [
            "Equal red, green and blue gives a shade of gray.",
            "0 on every channel is black, 255 on every channel is white.",
        ]
    lit = [name for name, v in (("red", r), ("green", g), ("blue", b)) if v >= 200]
    mixes = {
        ("red", "green"): "Red + green light makes yellow.",
        ("green", "blue"): "Green + blue light makes cyan.",
        ("red", "blue"): "Red + blue light makes magenta.",
        ("red", "green", "blue"): "All three at full strength make white.",
        ("red",): "Mostly red light, so you see red.",
        ("green",): "Mostly green light, so you see green.",
        ("blue",): "Mostly blue light, so you see blue.",
    }
    first = mixes.get(tuple(lit), "Try pushing one or two sliders to 255.")
    return [
        first,
        "Screens add light together, so more of a channel means brighter.",
        "Each channel is one byte: 0 (off) to 255 (full).",
    ]


sliders = [
    Slider(50, 320, 700, "Red", (235, 70, 70), 90),
    Slider(50, 400, 700, "Green", (70, 200, 110), 140),
    Slider(50, 480, 700, "Blue", (80, 130, 245), 230),
]

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        for s in sliders:
            s.handle(event)

    r, g, b = (s.value for s in sliders)
    h, l, sat = colorsys.rgb_to_hls(r / 255, g / 255, b / 255)

    # Draw every frame, not only when an event happens.
    screen.fill(BLACK)

    # Color preview
    pygame.draw.rect(screen, (r, g, b), (50, 30, 450, 190), border_radius=14)

    # Readouts
    readouts = [
        f"RGB  ({r}, {g}, {b})",
        f"HEX  #{r:02X}{g:02X}{b:02X}",
        f"HSL  ({round(h * 360)}\u00b0, {round(sat * 100)}%, {round(l * 100)}%)",
    ]
    for i, line in enumerate(readouts):
        screen.blit(font.render(line, True, WHITE), (530, 50 + i * 36))

    # Learning notes
    for i, line in enumerate(describe(r, g, b)):
        screen.blit(small.render(line, True, (190, 190, 220)), (50, 235 + i * 22))

    for s in sliders:
        s.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
