## 창을 띄워 미로를 생성하고 해결
import pygame
import sys

class Button:
    def __init__(self, text, x, y, width, height):
        self.text = text
        self.rect = pygame.Rect(x, y, width, height)

    def draw(self, surface):
        pygame.draw.rect(surface, (200, 200, 200), self.rect)
        text_surface = font.render(self.text, True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=self.rect.center)
        surface.blit(text_surface, text_rect)

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)

# make 함수 정의
def make():
    grid[2][2] = 1  # 그리드의 각 칸을 1로 초기화 (예시)

# 그리드 그리기
def draw_grid(n):
    print("test")
    cell_size = screen_size[0] // n
    for i in range(n):
        for j in range(n):
            rect = pygame.Rect(j * cell_size, i * cell_size + 60, cell_size, cell_size)
            if grid[i][j] == 1:
                color = (0, 255, 0)  # 그리드 칸이 활성화되면 초록색
            else:
                color = (200, 200, 200)  # 기본 색상
            pygame.draw.rect(screen, color, rect, 0)
            pygame.draw.rect(screen, (0, 0, 0), rect, 2)  # 경계선

# Pygame 초기화
pygame.init()

font = pygame.font.Font(None, 36)

# 화면 크기와 색상 설정
screen_size = (1024, 1024)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption('5x5 그리드 예제')
button_color = (0, 128, 255)
button_hover_color = (0, 255, 255)
button_rect = pygame.Rect(0, 0, 100, 50)

generate_button = Button("Generate", 0, 0, 100, 50)
solve_button = Button("Solve", 110, 0, 100, 50)

# 그리드 설정
grid_size = 10

grid = [[0 for _ in range(grid_size)] for _ in range(grid_size)]

# 메인 루프
running = True
is_draw = False
active = False
color_inactive = pygame.Color('lightskyblue3')
color_active = pygame.Color('dodgerblue2')
color = color_inactive
text = ''

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if generate_button.is_clicked(event.pos):
                is_draw = True
            if solve_button.is_clicked(event.pos):
                make()
            if input_box.collidepoint(event.pos):
                active = not active
            color = color_active if active else color_inactive

                
        if event.type == pygame.KEYDOWN:
            if active:
                if event.key == pygame.K_RETURN:
                    print("입력된 값:", text)
                    grid_size = int(text)
                    grid = [[0 for _ in range(grid_size)] for _ in range(grid_size)]
                    text = ''
                elif event.key == pygame.K_BACKSPACE:
                    text = text[:-1]
                else:
                    text += event.unicode

    # 화면 업데이트
    screen.fill((255, 255, 255))  # 배경색 흰색
    if is_draw:
        draw_grid(grid_size)  # 그리드 그리기
    generate_button.draw(screen)
    solve_button.draw(screen)  # 버튼 그리기
    
    # 입력 박스 그리기
    input_box = pygame.Rect(220, 0, 100, 50)
    pygame.draw.rect(screen, (200, 200, 200), input_box, 2)
    text_surface = font.render(text, True, (200, 200, 200))
    screen.blit(text_surface, (input_box.x + 5, input_box.y + 5))
    
    pygame.display.flip()

# Pygame 종료
pygame.quit()
sys.exit()
