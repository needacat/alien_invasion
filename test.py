import pygame

pygame.init()

# 设置游戏窗口大小和标题
screen_width, screen_height = 640, 480
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("提示窗口示例")

# 创建一个字体对象
font = pygame.font.Font(None, 30)

# 创建一个提示窗口 Surface 对象
prompt_surface = pygame.Surface((300, 100))
prompt_surface.fill(pygame.Color('white'))

# 在提示窗口上绘制文本
prompt_text = font.render("This is a window", True, pygame.Color('black'))
text_rect = prompt_text.get_rect(center=(150, 50))
prompt_surface.blit(prompt_text, text_rect)

# 创建一个按钮对象
button_rect = pygame.Rect(250, 400, 100, 50)
button_color = pygame.Color('gray')
button_text = font.render("Tips", True, pygame.Color('white'))
button_text_rect = button_text.get_rect(center=button_rect.center)

# 游戏主循环
running = True
show_prompt = False
while running:
    # 处理事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if button_rect.collidepoint(event.pos):
                show_prompt = True

    # 绘制游戏界面
    screen.fill(pygame.Color('white'))
    pygame.draw.rect(screen, button_color, button_rect)
    screen.blit(button_text, button_text_rect)

    # 如果需要显示提示窗口，绘制提示窗口和遮罩层
    if show_prompt:
        mask_surface = pygame.Surface((screen_width, screen_height))
        mask_surface.fill(pygame.Color(0, 0, 0, 128))
        prompt_rect = prompt_surface.get_rect(center=(screen_width // 2, screen_height // 2))
        screen.blit(mask_surface, (0, 0))
        screen.blit(prompt_surface, prompt_rect)

    # 更新屏幕显示
    pygame.display.update()

pygame.quit()
