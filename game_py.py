import pygame
import sys
import random
import pyttsx3  # Voice engine

# Initialize pygame
pygame.init()

# Initialize voice engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Set speaking speed

def speak(text):
    engine.say(text)
    engine.runAndWait()

# Screen setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("🐍 Snake Water Gun Game 🔫💧")

# Fonts and Colors
font = pygame.font.SysFont("arial", 36, bold=True)
big_font = pygame.font.SysFont("arial", 48, bold=True)
shadow_color = (50, 50, 50)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 150, 255)
GREEN = (0, 200, 100)
RED = (255, 100, 100)
HOVER = (255, 255, 180)

# Choices and Results
choices = ['snake', 'water', 'gun']
result_text = ""
user_score = 0
comp_score = 0

# Button class
class Button:
    def __init__(self, text, x, y, w, h, color, action=None):
        self.rect = pygame.Rect(x, y, w, h)
        self.default_color = color
        self.color = color
        self.text = text
        self.action = action

    def draw(self):
        pygame.draw.rect(screen, self.color, self.rect, border_radius=15)
        text_surface = font.render(self.text, True, BLACK)
        screen.blit(text_surface, (
            self.rect.x + (self.rect.width - text_surface.get_width()) // 2,
            self.rect.y + (self.rect.height - text_surface.get_height()) // 2))

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)

    def update_color(self, pos):
        if self.is_clicked(pos):
            self.color = HOVER
        else:
            self.color = self.default_color

# Game logic
def get_result(user, computer):
    if user == computer:
        return "Draw"
    elif (user == "snake" and computer == "water") or \
         (user == "water" and computer == "gun") or \
         (user == "gun" and computer == "snake"):
        return "You Win"
    else:
        return "Computer Wins"

# Buttons
buttons = [
    Button("🐍 Snake", 100, 400, 150, 60, BLUE, action="snake"),
    Button("💧 Water", 325, 400, 150, 60, GREEN, action="water"),
    Button("🔫 Gun",   550, 400, 150, 60, RED, action="gun"),
]

# Draw fancy background
def draw_background():
    for y in range(HEIGHT):
        color = (100 + y//10, 150 - y//15, 255 - y//12)
        pygame.draw.line(screen, color, (0, y), (WIDTH, y))

# Draw shadowed text
def draw_shadowed_text(text, x, y, font, color):
    shadow = font.render(text, True, shadow_color)
    screen.blit(shadow, (x+2, y+2))
    main_text = font.render(text, True, color)
    screen.blit(main_text, (x, y))

# Main loop
running = True
while running:
    draw_background()
    mouse_pos = pygame.mouse.get_pos()

    # Title
    draw_shadowed_text("🎮 Snake Water Gun 🎮", WIDTH//2 - 200, 30, big_font, WHITE)

    # Buttons
    for btn in buttons:
        btn.update_color(mouse_pos)
        btn.draw()

    # Result text
    draw_shadowed_text(result_text, WIDTH//2 - 300, 120, font, WHITE)

    # Score text
    score_text = f"👤 You: {user_score}   🤖 Computer: {comp_score}"
    draw_shadowed_text(score_text, WIDTH//2 - 200, 180, font, WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT or (
            event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            pygame.quit()
            sys.exit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            for btn in buttons:
                if btn.is_clicked(mouse_pos):
                    user_choice = btn.action
                    comp_choice = random.choice(choices)
                    outcome = get_result(user_choice, comp_choice)
                    result_text = f"You chose {user_choice}, Computer chose {comp_choice} → {outcome}"

                    if outcome == "You Win":
                        user_score += 1
                    elif outcome == "Computer Wins":
                        comp_score += 1

                    # Speak the result
                    speak(result_text)

    pygame.display.update()
