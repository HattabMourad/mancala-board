import pygame
import sys
from script import MancalaGame, Play

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 400
PIT_RADIUS = 30
STORE_WIDTH, STORE_HEIGHT = 60, 120
FONT_SIZE = 24
BACKGROUND_COLOR = (255, 204, 153)
PIT_COLOR = (204, 102, 0)
STORE_COLOR = (153, 51, 0)
TEXT_COLOR = (0, 0, 0)

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Mancala")
font = pygame.font.Font(None, FONT_SIZE)

def draw_text(text, x, y):
    label = font.render(text, True, TEXT_COLOR)
    screen.blit(label, (x, y))

def draw_board(game):
    screen.fill(BACKGROUND_COLOR)

    pits = game.state.board
    for i, pit in enumerate(game.state.player1_pits):
        x, y = 150 + i * 100, 300
        pygame.draw.circle(screen, PIT_COLOR, (x, y), PIT_RADIUS)
        draw_text(f"{pit}\n{pits[pit]}", x - 10, y - 10)

    for i, pit in enumerate(game.state.player2_pits[::-1]):
        x, y = 150 + i * 100, 100
        pygame.draw.circle(screen, PIT_COLOR, (x, y), PIT_RADIUS)
        draw_text(f"{pit}\n{pits[pit]}", x - 10, y - 10)

    pygame.draw.rect(screen, STORE_COLOR, pygame.Rect(50, 100, STORE_WIDTH, STORE_HEIGHT))
    pygame.draw.rect(screen, STORE_COLOR, pygame.Rect(700, 100, STORE_WIDTH, STORE_HEIGHT))
    draw_text(str(pits[1]), 70, 170)
    draw_text(str(pits[2]), 720, 170)

    pygame.display.flip()

def main():
    clock = pygame.time.Clock()
    running = True

    mode = None
    while mode is None:
        screen.fill(BACKGROUND_COLOR)
        draw_text("Choose Mode:", SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 - 60)
        draw_text("1. Human vs Computer", SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 - 30)
        draw_text("2. Computer vs Computer", SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    mode = "human_vs_computer"
                elif event.key == pygame.K_2:
                    mode = "computer_vs_computer"

    game = MancalaGame(player1_side="human" if mode == "human_vs_computer" else "computer")

    is_human_turn = True if mode == "human_vs_computer" else False
    computer1_wins = 0
    computer2_wins = 0

    while running:
        draw_board(game)

        if game.gameOver():
            winner, score = game.findWinner()
            if mode == "computer_vs_computer":
                if winner == "COMPUTER":
                    if computer1_wins > computer2_wins:
                        result_text = "Computer 1 (Minimax) Wins!"
                    elif computer2_wins > computer1_wins:
                        result_text = "Computer 2 (Alpha-Beta Pruning) Wins!"
                    else:
                        result_text = "It's a Tie!"
                else:
                    result_text = f"Tie with score {score} seeds."
            else:
                result_text = f"Game Over! Winner: {winner} with {score} seeds."
            draw_text(result_text, SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2)
            pygame.display.flip()
            pygame.time.wait(5000)
            running = False
            continue

        if mode == "human_vs_computer" and is_human_turn:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    mouse_x, mouse_y = event.pos
                    for i, pit in enumerate(game.state.player1_pits):
                        x, y = 150 + i * 100, 300
                        if (mouse_x - x) ** 2 + (mouse_y - y) ** 2 <= PIT_RADIUS ** 2:
                            try:
                                extra_turn = game.state.doMove(1, pit)
                                is_human_turn = extra_turn
                            except ValueError as e:
                                print(e)

        elif mode == "computer_vs_computer" or not is_human_turn:
            if mode == "computer_vs_computer":
                if is_human_turn:
                    _, move = Play.Minimax(game, "MAX", 5)
                    game.state.doMove(1, move)
                    computer1_wins += 1
                else:
                    _, move = Play.MinimaxAlphaBetaPruning(game, "MIN", 5, -float('inf'), float('inf'))
                    game.state.doMove(2, move)
                    computer2_wins += 1
                is_human_turn = not is_human_turn
            else:
                _, move = Play.MinimaxAlphaBetaPruning(game, "MAX", 5, -float('inf'), float('inf'))
                game.state.doMove(2, move)
                is_human_turn = not mode == "computer_vs_computer"

        pygame.time.delay(1000 if mode == "computer_vs_computer" else 0)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        clock.tick(30)

if __name__ == "__main__":
    main()
