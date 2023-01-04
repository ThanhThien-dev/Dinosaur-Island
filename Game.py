import pygame
import sys
import random
import math

WIDTH = 900
HEIGHT = 390

# Khởi tạo Pygame
pygame.mixer.pre_init(frequency=44100, size=-16, channels=2, buffer=512)
pygame.init()

# Âm thanh trong game
pygame.mixer.init()

# Tạo cửa sổ game với kích thước 900x390
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Tạo tiêu đề và icon cho game
pygame.display.set_caption('DINOSAUR ISLAND')
icon = pygame.image.load('assets\img\icon.png')
pygame.display.set_icon(icon)

# Tạo lớp Background
class BG:
    
    # Phương thức khởi tạo
    def __init__(self, x):
        self.width = WIDTH
        self.height = HEIGHT
        self.x = x
        self.y = 0
        self.set_texture()
        self.show()
        
    # Phương thức cập nhật
    def update(self, def_x):
        self.x += def_x
        if self.x <= -WIDTH:
            self.x = WIDTH
    
    # Phương thức hiển thị    
    def show(self):
        screen.blit(self.texture, (self.x, self.y))
    
    # Phương thức kết cấu    
    def set_texture(self):
        self.texture = pygame.image.load(r'assets\img\bg.png')
        
# Tạo lớp Dino
class Dino:
    
    def __init__(self):
        self.width = 64
        self.height = 68
        self.x = 80
        self.y = 270
        self.img_num = 0
        self.def_y = 7
        self.gra = 1.5 # Biến trọng lực
        self.running = True # Trạng thái đang chạy trên mặt đất
        self.jumping = False # Trạng thái đang nhảy
        self.falling = False # Trạng thái đáp đất
        self.jump_to = 110 # Nhảy đến độ cao
        self.floor = self.y
        self.set_texture()
        self.set_sound()
        self.show()
    
    def update(self, loop):
        # Trạng thái đang nhảy
        if self.jumping:
            self.y -= self.def_y
            if self.y <= self.jump_to:
                self.fall()
        
        # Trạng thái đang đáp đất
        elif self.falling:
            self.y += self.gra * self.def_y
            if self.y >= self.floor:
                self.run()
        
        # Trạng thái đang chạy
        elif self.running and loop % 4 == 0: # Điều chỉnh tốc độ hoạt ảnh của nhân vật
            self.img_num = (self.img_num + 1) % 9 # Giống như một vòng lặp, self.img_num có giá trị lớn hơn 8, nó sẽ được gán lại bằng 0.
            self.set_texture()
    
    def show(self):
        screen.blit(self.texture, (self.x, self.y))
    
    def set_texture(self):
        self.texture = pygame.image.load(f'assets\img\dino\dino{self.img_num}.png')
        
    def set_sound(self):
        self.sound = pygame.mixer.Sound('assets\sound\jump.wav')
        
    def jump(self):
        self.sound.play()
        self.jumping = True
        self.running = False
        
    def fall(self):
        self.falling = True
        self.jumping = False
        
    def run(self):
        self.running = True
        self.falling = False   

# Tạo lớp Dino tiến hóa cấp 1
class Lv1:
    
    def __init__(self):
        self.width = 64
        self.height = 68
        self.x = 80
        self.y = Dino().y
        self.img_num = 0
        self.def_y = 7
        self.gra = 1.5 # Biến trọng lực
        self.running = True # Trạng thái đang chạy trên mặt đất
        self.jumping = False # Trạng thái đang nhảy
        self.falling = False # Trạng thái đáp đất
        self.jump_to = 110 # Nhảy đến độ cao
        self.floor = self.y
        self.set_texture()
        self.set_sound()
        self.show()
        
    def update(self, loop):
        # Trạng thái đang nhảy
        if self.jumping:
            self.y -= self.def_y
            if self.y <= self.jump_to:
                self.fall()
        
        # Trạng thái đang đáp đất
        elif self.falling:
            self.y += self.gra * self.def_y
            if self.y >= self.floor:
                self.run()
        
        # Trạng thái đang chạy
        elif self.running and loop % 4 == 0: # Khi loop bằng 0 thì các giá trị được thực thi
            self.img_num = (self.img_num + 1) % 3 #self.img_num có giá trị lớn hơn 3, nó sẽ được gán lại bằng 0.
            self.set_texture()
    
    def show(self):
        screen.blit(self.texture, (self.x, self.y))
    
    def set_texture(self):
        self.texture = pygame.image.load(f'assets\img\dino\lv1dino{self.img_num}.png')
        
    def set_sound(self):
        self.sound = pygame.mixer.Sound('assets\sound\jump.wav')
        
    def jump(self):
        self.sound.play()
        self.jumping = True
        self.running = False
        
    def fall(self):
        self.falling = True
        self.jumping = False
        
    def run(self):
        self.running = True
        self.falling = False
        
# Tạo lớp Dino tiến hóa cấp 2
class Lv2:
    
    def __init__(self):
        self.width = 64
        self.height = 68
        self.x = 80
        self.y = Dino().y
        self.img_num = 0
        self.def_y = 7
        self.gra = 1.5 # Biến trọng lực
        self.running = True # Trạng thái đang chạy trên mặt đất
        self.jumping = False # Trạng thái đang nhảy
        self.falling = False # Trạng thái đáp đất
        self.jump_to = 110 # Nhảy đến độ cao
        self.floor = self.y
        self.set_texture()
        self.set_sound()
        self.show()
        
    def update(self, loop):
        # Trạng thái đang nhảy
        if self.jumping:
            self.y -= self.def_y
            if self.y <= self.jump_to:
                self.fall()
        
        # Trạng thái đang đáp đất
        elif self.falling:
            self.y += self.gra * self.def_y
            if self.y >= self.floor:
                self.run()
        
        # Trạng thái đang chạy
        elif self.running and loop % 4 == 0: # Khi loop bằng 0 thì các giá trị được thực thi
            self.img_num = (self.img_num + 1) % 8 #self.img_num có giá trị lớn hơn 8, nó sẽ được gán lại bằng 0.
            self.set_texture()
    
    def show(self):
        screen.blit(self.texture, (self.x, self.y))
    
    def set_texture(self):
        self.texture = pygame.image.load(f'assets\img\dino\lv2dino{self.img_num}.png')
        
    def set_sound(self):
        self.sound = pygame.mixer.Sound('assets\sound\jump.wav')
        
    def jump(self):
        self.sound.play()
        self.jumping = True
        self.running = False
        
    def fall(self):
        self.falling = True
        self.jumping = False
        
    def run(self):
        self.running = True
        self.falling = False

# Tạo lớp Dino tiến hóa cấp 3
class Lv3:
    
    def __init__(self):
        self.width = 64
        self.height = 68
        self.x = 80
        self.y = Dino().y
        self.img_num = 0
        self.def_y = 7
        self.gra = 1.5 # Biến trọng lực
        self.running = True # Trạng thái đang chạy trên mặt đất
        self.jumping = False # Trạng thái đang nhảy
        self.falling = False # Trạng thái đáp đất
        self.jump_to = 110 # Nhảy đến độ cao
        self.floor = self.y
        self.set_texture()
        self.set_sound()
        self.show()
        
    def update(self, loop):
        # Trạng thái đang nhảy
        if self.jumping:
            self.y -= self.def_y
            if self.y <= self.jump_to:
                self.fall()
        
        # Trạng thái đang đáp đất
        elif self.falling:
            self.y += self.gra * self.def_y
            if self.y >= self.floor:
                self.run()
        
        # Trạng thái đang chạy
        elif self.running and loop % 4 == 0: # Khi loop bằng 0 thì các giá trị được thực thi
            self.img_num = (self.img_num + 1) % 8 #self.img_num có giá trị lớn hơn 8, nó sẽ được gán lại bằng 0.
            self.set_texture()
    
    def show(self):
        screen.blit(self.texture, (self.x, self.y))
    
    def set_texture(self):
        self.texture = pygame.image.load(f'assets\img\dino\lv3dino{self.img_num}.png')
        
    def set_sound(self):
        self.sound = pygame.mixer.Sound('assets\sound\jump.wav')
        
    def jump(self):
        self.sound.play()
        self.jumping = True
        self.running = False
        
    def fall(self):
        self.falling = True
        self.jumping = False
        
    def run(self):
        self.running = True
        self.falling = False
        
# Tạo lớp Dino tiến hóa cấp 4
class Lv4:
    
    def __init__(self):
        self.width = 64
        self.height = 68
        self.x = 80
        self.y = Dino().y
        self.img_num = 0
        self.def_y = 7
        self.gra = 1.5 # Biến trọng lực
        self.running = True # Trạng thái đang chạy trên mặt đất
        self.jumping = False # Trạng thái đang nhảy
        self.falling = False # Trạng thái đáp đất
        self.jump_to = 110 # Nhảy đến độ cao
        self.floor = self.y
        self.set_texture()
        self.set_sound()
        self.show()
        
    def update(self, loop):
        # Trạng thái đang nhảy
        if self.jumping:
            self.y -= self.def_y
            if self.y <= self.jump_to:
                self.fall()
        
        # Trạng thái đang đáp đất
        elif self.falling:
            self.y += self.gra * self.def_y
            if self.y >= self.floor:
                self.run()
        
        # Trạng thái đang chạy
        elif self.running and loop % 4 == 0: # Khi loop bằng 0 thì các giá trị được thực thi
            self.img_num = (self.img_num + 1) % 5 #self.img_num có giá trị lớn hơn 5, nó sẽ được gán lại bằng 0.
            self.set_texture()
    
    def show(self):
        screen.blit(self.texture, (self.x, self.y))
    
    def set_texture(self):
        self.texture = pygame.image.load(f'assets\img\dino\lv4dino{self.img_num}.png')
        
    def set_sound(self):
        self.sound = pygame.mixer.Sound('assets\sound\jump.wav')
        
    def jump(self):
        self.sound.play()
        self.jumping = True
        self.running = False
        
    def fall(self):
        self.falling = True
        self.jumping = False
        
    def run(self):
        self.running = True
        self.falling = False

# Tạo lớp chướng ngại vật
class Gun:
    
    def __init__(self, x):
        self.width = 113
        self.height = 90
        self.x = x
        self.y = 270
        self.set_texture()
        self.show()
    
    def update(self, def_x):
        self.x += def_x
    
    def show(self):
        screen.blit(self.texture, (self.x, self.y))
    
    def set_texture(self):
        self.texture = pygame.image.load(r'assets\img\obstacle\gun.png')

# Kiểm tra va chạm
class Collision:
    
    def between(self, obj1, obj2):
        distance = math.sqrt( (obj1.x - obj2.x)**2 + (obj1.y - obj2.y)**2 )
        return distance < 50 # Trả về giá trị boolean, nếu khoảng cách nhỏ hơn 50 thì xảy ra va chạm

# Tạo lớp điểm số
class Score:
    
    def __init__(self, hscore):
        self.score = 0
        self.hscore = hscore
        self.font_score = pygame.font.SysFont('monospace', 38, bold=True)
        self.font_hscore = pygame.font.SysFont('monospace', 20)
        self.color = (0, 0, 0)
        self.set_sound()
        self.show()
        
    def update(self, loop):
        self.score = loop // 10
        self.check_hscore()
        self.check_sound()
        
    def set_sound(self):
        self.sound = pygame.mixer.Sound('assets\sound\point.wav')
        
    def check_hscore(self):
        if self.score >= self.hscore:
            self.hscore = self.score
            
    def check_sound(self):
        if self.score % 50 == 0 and self.score != 0:
            self.sound.play()
    
    def show(self):
        self.label1 = self.font_hscore.render(f'High Score: {self.hscore}' , True, self.color)
        self.label2 = self.font_score.render(f'{self.score}m', True, self.color)
        lable_width = self.label1.get_rect().width
        screen.blit(self.label1, (WIDTH - lable_width - 10, 10))
        screen.blit(self.label2, (WIDTH // 2 - 35, 70))

# Tạo lớp trò chơi    
class Game:
        
    def __init__(self, hscore = 0):
        self.bg = [BG(0), BG(WIDTH)]
        self.dino = Dino()
        self.lv1 = Lv1()
        self.lv2 = Lv2()
        self.lv3 = Lv3()
        self.lv4 = Lv4()
        self.obstacle = []
        self.collision = Collision()
        self.score = Score(hscore)
        self.playing = False
        self.speed = 5
        self.appear_gun()
        self.set_sound()
        self.set_labels()
        
    def set_sound(self):
        self.sound = pygame.mixer.Sound('assets\sound\die.wav')
        
    def set_labels(self):
        
        big_font = pygame.font.SysFont('monospace', 38, bold=True)
        small_font = pygame.font.SysFont('monospace', 28)
        self.big_label = big_font.render(f'G A M E  O V E R', True, (0, 0, 0))
        self.small_label = small_font.render(f'Nhấn phím ENTER để bắt đầu lại', True, (0, 0, 0))
        
    def start(self):
        self.playing = True
        
    def end(self):
        self.sound.play()
        bg_end = pygame.image.load(r'assets\img\end.png')
        dino1 = pygame.image.load(r'assets\img\dino\dino0.png')
        dino2 = pygame.image.load(r'assets\img\dino\1dino0.png')
        dino3 = pygame.image.load(r'assets\img\dino\2dino0.png')
        dino4 = pygame.image.load(r'assets\img\dino\3dino0.png')
        dino5 = pygame.image.load(r'assets\img\dino\4dino0.png')
        screen.blit(bg_end, (0,0))
        screen.blit(self.big_label, (WIDTH // 2 - self.big_label.get_width() // 2, HEIGHT // 3))
        screen.blit(self.small_label, (WIDTH // 2 - self.small_label.get_width() // 2 - 5, HEIGHT // 2))
        screen.blit(dino1, (WIDTH // 2 - self.small_label.get_width() // 2, 260))
        screen.blit(dino2, ((WIDTH // 2 - self.small_label.get_width() // 2) + 100, 260))
        screen.blit(dino3, ((WIDTH // 2 - self.small_label.get_width() // 2) + 200, 260))
        screen.blit(dino4, ((WIDTH // 2 - self.small_label.get_width() // 2) + 300, 260))
        screen.blit(dino5, ((WIDTH // 2 - self.small_label.get_width() // 2) + 400, 260))
        
        self.playing = False
        
    def appear(self, loop):
        return loop % 10 == 0 # Xuất hiện khi con số chia hết cho 100 (Tránh dồn dập)
    
    def appear_gun(self):
        # Danh sách viên đạn
        if len(self.obstacle) > 0:
            pre_gun = self.obstacle[-1] # Lấy vị trí viên đạn cuối cùng
            x = random.randint(pre_gun.x + self.dino.width + 155, WIDTH + pre_gun.x + self.dino.width + 155) # self.dino.width là chiều rộng của con Dino, 155 là một giá trị ngẫu nhiên để tăng độ rộng đó
        
        # Mảng trống
        else:
            x = random.randint(WIDTH + 300, 1200)
        
        # Tạo ra viên đạn mới
        gun = Gun(x)
        self.obstacle.append(gun)

    def Uplv1(self):
        if self.score.score > 50 and self.score.score <= 100:
            return True
        
    def Uplv2(self):
        if self.score.score > 100 and self.score.score <= 150:
            return True
        
    def Uplv3(self):
        if self.score.score > 150 and self.score.score <= 200:
            return True
        
    def Uplv4(self):
        if self.score.score > 200:
            return True

    def restart(self):
        self.__init__(hscore = self.score.hscore)

# Vòng lặp chính của game
def main():
    
    # Objects
    game = Game()
    dino = game.dino
    lv1 = game.lv1
    lv2 = game.lv2
    lv3 = game.lv3
    lv4 = game.lv4
    
    # Variables
    loop = 0
    end = False
    
    clock = pygame.time.Clock()
    
    # Vòng lặp chính
    while True:
        
        if game.playing:
            
            loop += 1
            
            # BACKGROUND
            for bg in game.bg:
                bg.update(-game.speed)
                bg.show()
                
            # DINO
            dino.update(loop)
            dino.show()
            
            # Tiến hóa và tăng độ khó khi đạt mỗi 50 điểm
            if game.Uplv1():
                dino = lv1
                x += 0.02
                if x > 70:
                    x = 70
                print('Giá trị FPS LV1: ',x)
                clock.tick(x)
                
            elif game.Uplv2():
                dino = lv2
                x += 0.02
                if x > 80:
                    x = 80
                print('Giá trị FPS LV2: ',x)
                clock.tick(x)
                
            elif game.Uplv3():
                dino = lv3
                x += 0.02
                if x > 90:
                    x = 90
                print('Giá trị FPS LV3: ',x)
                clock.tick(x)
                
            elif game.Uplv4():
                dino = lv4
                x += 0.02
                print('Giá trị FPS LV4: ',x)
                clock.tick(x)
                
            else:
                x = 60
                print('Giá trị FPS ban đầu: ',x)
                clock.tick(x)
            
            # OBSTACLE
            if game.appear(loop):
                game.appear_gun()
            
            for gun in game.obstacle:
                gun.update(-game.speed)
                gun.show()
                
                # Xảy ra va chạm
                if game.collision.between(dino, gun):
                    end = True
                    
            if end:
                game.end()
                    
            # SCORE
            game.score.update(loop)
            game.score.show()
        
        # Xử lý sự kiện người dùng
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == pygame.KEYDOWN:    
                if event.key == pygame.K_SPACE:
                    if not end:
                        if dino.running:
                            dino.jump()
                            
                        if not game.playing:
                            game.start()
                        
                if event.key == pygame.K_RETURN:
                    game.restart()
                    dino = game.dino
                    loop = 0
                    end = False
        
        pygame.display.update()

# Tạo màn hình bắt đầu
class Stcreen:
    
    def __init__(self):
        self.flash = True
        self.set_sound()
        self.set_texture()
        self.show()
        self.title()
        
    def set_sound(self):
        self.sound = pygame.mixer.Sound('assets\sound\start.wav')
        
    def title(self):
        # Tính toán chu kỳ nhấp nháy của phông chữ, true là hiện, false là ẩn
        self.current_time = pygame.time.get_ticks()
        
        if self.current_time % 1000 < 500:
            self.flash = True # Chữ hiện
        else:
            self.flash = False # Chữ ẩn

        # Hiển thị phông chữ theo trạng thái flash
        if self.flash:
            font = pygame.font.SysFont('monospace', 20, bold=True)
            self.text = font.render("Nhấn phím bất kì để bắt đầu", True, (0, 0, 0))
            screen.blit(self.text, (WIDTH // 2 - 140, HEIGHT // 2 + 120))
    
    def show(self):
        screen.blit(self.texture, (0, 0))
        self.sound.play()
        self.title()

    def set_texture(self):
        self.texture = pygame.image.load(r'assets\img\screen.png')

def menu():
    
    stscreen = Stcreen()
    stscreen.sound.play()

    while True:
        
        stscreen.show()
       
        pygame.display.update()
        
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == pygame.KEYDOWN:
                stscreen.sound.stop()
                main()

menu()