import pygame
import random

# Inicializa o Pygame
pygame.init()

# Configurações da tela
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Top-Down Adventure")

# Cores
WHITE = (255, 255, 255)
RED = (200, 50, 50)
GREEN = (50, 200, 50)
BLUE = (50, 50, 200)
BLACK = (0, 0, 0)

# Fonte
font = pygame.font.Font(None, 36)

# Configurações do jogador
player_x, player_y = WIDTH // 2, HEIGHT // 2
player_speed = 4
score = 0
game_over = False
zoom = 1.0  # Redução do zoom para melhor visualização

# Loja
shop_open = False
upgrades = {"speed": 100, "shield": 200}

# Inimigos
enemy_types = ["normal", "fast", "slow", "shooter", "growing", "thief"]
enemies = []
spawned_enemy_types = set()
max_enemies = 10  # Limite máximo de inimigos ativos
items = []

# Função para reiniciar o jogo
def reset_game():
    global player_x, player_y, score, game_over, enemies, items, shop_open, spawned_enemy_types
    player_x, player_y = WIDTH // 2, HEIGHT // 2
    score = 0
    game_over = False
    shop_open = False
    enemies = []
    spawned_enemy_types = set()
    items = [pygame.Rect(random.randint(0, WIDTH), random.randint(0, HEIGHT), 20, 20) for _ in range(5)]

reset_game()
clock = pygame.time.Clock()

running = True
while running:
    screen.fill(WHITE)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keys = pygame.key.get_pressed()
    
    if not game_over and not shop_open:
        # Movimentação
        if keys[pygame.K_a]: player_x -= player_speed
        if keys[pygame.K_d]: player_x += player_speed
        if keys[pygame.K_w]: player_y -= player_speed
        if keys[pygame.K_s]: player_y += player_speed

        # Adiciona inimigos de forma controlada
        if len(enemies) < max_enemies:
            enemy_index = min(score // 1000, len(enemy_types) - 1)
            if enemy_types[enemy_index] not in spawned_enemy_types:
                new_type = enemy_types[enemy_index]
                enemies.append({"type": new_type, "x": random.randint(0, WIDTH), "y": random.randint(0, HEIGHT), "speed": random.randint(1, 3)})
                spawned_enemy_types.add(new_type)
        
        # Movimenta inimigos e verifica colisão
        for enemy in enemies:
            if enemy["x"] < player_x:
                enemy["x"] += enemy["speed"]
            elif enemy["x"] > player_x:
                enemy["x"] -= enemy["speed"]
            if enemy["y"] < player_y:
                enemy["y"] += enemy["speed"]
            elif enemy["y"] > player_y:
                enemy["y"] -= enemy["speed"]
            
            # Verifica colisão com o jogador
            if pygame.Rect(player_x, player_y, 40, 40).colliderect(pygame.Rect(enemy["x"], enemy["y"], 30, 30)):
                game_over = True
        
        # Desenha jogador
        pygame.draw.rect(screen, BLUE, ((WIDTH//2) - (20 * zoom), (HEIGHT//2) - (20 * zoom), 40 * zoom, 40 * zoom))

        # Desenha inimigos
        for enemy in enemies:
            color = RED if enemy["type"] == "normal" else BLACK
            pygame.draw.rect(screen, color, (enemy["x"] - player_x + WIDTH//2, enemy["y"] - player_y + HEIGHT//2, 30 * zoom, 30 * zoom))

        # Desenha itens e verifica coleta
        for item in items[:]:
            pygame.draw.rect(screen, GREEN, (item.x - player_x + WIDTH//2, item.y - player_y + HEIGHT//2, 20 * zoom, 20 * zoom))
            if pygame.Rect(player_x, player_y, 40, 40).colliderect(item):
                items.remove(item)
                score += 100
                # Reposiciona um novo item
                items.append(pygame.Rect(random.randint(0, WIDTH), random.randint(0, HEIGHT), 20, 20))
        
        # Exibir pontuação
        score_text = font.render(f"Score: {score}", True, BLACK)
        screen.blit(score_text, (10, 10))
    
    elif shop_open:
        screen.fill(BLACK)
        shop_text = font.render("Loja: (1) Velocidade - 100 pts | (2) Escudo - 200 pts", True, WHITE)
        screen.blit(shop_text, (50, HEIGHT//2))
        if keys[pygame.K_1] and score >= 100:
            player_speed += 1
            score -= 100
        if keys[pygame.K_2] and score >= 200:
            score -= 200  # Implementar escudo depois

    pygame.display.flip()
    clock.tick(60)

pygame.quit()