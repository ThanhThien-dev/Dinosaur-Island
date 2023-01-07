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
    
    """
    Chức năng: Tạo một hình nền cho game.
    
    Args:
        x: Tọa độ x của hình nền.
    
    Input:
        width: Chiều rộng của hình nền.
        height: Chiều cao của hình nền.
        x: Tọa độ x của hình nền.
        y: Tọa độ y của hình nền.
        texture (Surface): Đối tượng Surface tạo từ hình ảnh của hình nền.
    
    Output:
        update(def_x): Cập nhật trạng thái của hình nền theo biến speed được khai báo ở class game di chuyển theo trục x.
        show(): Hiển thị hình nền lên màn hình.
        set_texture(): Tạo ra một đối tượng Surface từ hình ảnh của hình nền và lưu trữ trong thuộc tính self.texture.
    """
    
    # Hàm khởi tạo
    def __init__(self, x):
        
        """
            Chức năng: Tạo một đối tượng hình nền với tọa độ x cho trước và tạo ra một đối tượng Surface từ hình ảnh của hình nền.
        
        Args:
            x: Tọa độ x của hình nền dùng để tạo vòng lặp.
            
        Input:
            width: Chiều rộng của hình nền.
            height: Chiều cao của hình nền.
            x: Tọa độ x của hình nền.
            y: Tọa độ y của hình nền.
            texture (Surface): Đối tượng Surface tạo từ hình ảnh của hình nền.
        
        Output:
            BG: Đối tượng hình nền với thuộc tính width, height, x, y, texture được khởi tạo.
        """
    
        self.width = WIDTH
        self.height = HEIGHT
        self.x = x
        self.y = 0
        self.set_texture()
        self.show()
        
    # Hàm cập nhật
    def update(self, def_x):
        
        """
        Chức năng: Cập nhật tọa độ x của hình nền theo biến speed được khai báo ở class game di chuyển theo trục x. Nếu tọa độ x của hình nền nhỏ hơn hoặc bằng -WIDTH, thì sẽ đặt lại tọa độ x bằng WIDTH.
        
        Input:
            def_x: Độ dịch cần cập nhật tọa độ x.
        
        Output:
            x: Tọa độ x của hình nền.
        """
        
        self.x += def_x
        if self.x <= -WIDTH:
            self.x = WIDTH
    
    # Hàm hiển thị    
    def show(self):
        
        """
        Chức năng: Sử dụng phương thức blit() của module pygame để hiển thị đối tượng Surface của hình nền lên màn hình tại tọa độ x và y.
        
        Attributes:
            x: Tọa độ x của hình nền.
            y: Tọa độ y của hình nền.
            texture (Surface): Đối tượng Surface tạo từ hình ảnh của hình nền.
        """
        
        screen.blit(self.texture, (self.x, self.y))
    
    # Hàm surface dùng để load hình ảnh
    def set_texture(self):
        
        """
        Chức năng: Phương thức này dùng để load hình ảnh background vào chương trình.
        
        Input:
            Hình ảnh bg.png
            
        Output:
            Hình ảnh background
        """
        
        self.texture = pygame.image.load(r'assets\img\bg.png')
        
# Tạo lớp Dino
class Dino:
    
    """
    Chức năng: Class đại diện cho nhân vật khủng long trong game. Nó dùng để định nghĩa các phương thức khởi tạo, cập nhật, hiển thị
    , tạo đối tượng Surface từ hình ảnh và tạo đối tượng Sound từ âm thanh của nhân vật khủng long, cũng như các phương thức nhảy, rơi và chạy.
    
    Attributes:
        width (int): Chiều rộng của nhân vật khủng long.
        height (int): Chiều cao của nhân vật khủng long.
        x (int): Tọa độ x của nhân vật khủng long.
        y (int): Tọa độ y của nhân vật khủng long.
        img_num (int): Số thứ tự của hình ảnh hiện tại của nhân vật khủng long.
        def_y (int): Độ dịch theo trục y khi nhân vật khủng long nhảy.
        gra (float): Trọng lực của nhân vật khủng long.
        running (bool): Trạng thái đang chạy trên mặt đất.
        jumping (bool): Trạng thái đang nhảy.
        falling (bool): Trạng thái đang rơi.
        jump_to (int): Độ cao tối đa mà khủng long nhảy đến.
        floor (int): Định nghĩa tọa độ y của sàn.
        texture (pygame.Surface): Đối tượng Surface đại diện cho hình ảnh của nhân vật khủng long.
        sound (pygame.mixer.Sound): Đối tượng Sound đại diện cho âm thanh của nhân vật khủng long.
    """
    
    # Hàm khởi tạo
    def __init__(self):
        
        """
        Chức năng: Khởi tạo các giá trị và phương thức cho nhân vật Dino
        """
        
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
        self.lv = 0
        self.set_texture()
        self.set_sound()
        self.show()
    
    # Hàm cập nhật
    def update(self, loop):
        
        """
        Chức năng: Phương thức này cập nhật trạng thái nhảy, đáp đất và chạy của đối tượng Dino dựa trên trạng thái hiện tại và tọa độ y 
        của nó. Nếu đối tượng Dino đang nhảy, tọa độ y của nó sẽ bị giảm bằng khoảng trừ tọa độ y. Nếu đối tượng Dino đang đáp đất, tọa 
        độ y của nó sẽ tăng bằng tích của trọng lực và khoảng trừ tọa độ y. Nếu đối tượng Dino đang chạy và số vòng lặp hiện tại 
        chia hết cho 4, hình ảnh của đối tượng Dino sẽ thay đổi tạo ra hoạt ảnh.
        
        Args:
        loop (int): Số vòng lặp hiện tại.
        
        Returns:
            Trả về các trạng thái và thực hiện hành động ở trạng thái đó
        """
        
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
            if(self.lv == 0):
                self.img_num = (self.img_num + 1) % 9 # Giống như một vòng lặp, self.img_num có giá trị lớn hơn 8, nó sẽ được gán lại bằng 0.
                self.set_texture()
            if(self.lv == 1):
                self.img_num = (self.img_num + 1) % 3 #self.img_num có giá trị lớn hơn 3, nó sẽ được gán lại bằng 0.
                self.set_texture()
            if(self.lv == 2):
                self.img_num = (self.img_num + 1) % 8 #self.img_num có giá trị lớn hơn 8, nó sẽ được gán lại bằng 0.
                self.set_texture()
            if(self.lv == 3):
                self.img_num = (self.img_num + 1) % 8 #self.img_num có giá trị lớn hơn 8, nó sẽ được gán lại bằng 0.
                self.set_texture()
            if(self.lv == 4):
                self.img_num = (self.img_num + 1) % 5 #self.img_num có giá trị lớn hơn 5, nó sẽ được gán lại bằng 0.
                self.set_texture()
    
    # Hàm hiển thị
    def show(self):
        
        """
        Chức năng: Sử dụng phương thức blit() của module pygame để hiển thị đối tượng Surface của nhân vật Dino lên màn hình tại tọa độ x và y.
        
        Attributes:
            x: Tọa độ x của nhân vật Dino.
            y: Tọa độ y của nhân vật Dino.
            texture (Surface): Đối tượng Surface tạo từ hình ảnh của nhân vật Dino.
        """
        
        screen.blit(self.texture, (self.x, self.y))
    
    # Hàm surface
    def set_texture(self):
        
        """
        Chức năng: Phương thức này thiết lập hình ảnh của đối tượng Dino dựa trên số hình ảnh của nó.
        
        Input:
            img_num (int): Số thứ tự hình ảnh được định nghĩa từ 0 đến số cuối cùng của def init
            
        Output:
            Hình ảnh nhân vật Dino
        """
        if(self.lv == 0):
            self.texture = pygame.image.load(f'assets\img\dino\dino{self.img_num}.png')
        if(self.lv == 1):
            self.texture = pygame.image.load(f'assets\img\dino\lv1dino{self.img_num}.png')
        if(self.lv == 2):
            self.texture = pygame.image.load(f'assets\img\dino\lv2dino{self.img_num}.png')
        if(self.lv == 3):
            self.texture = pygame.image.load(f'assets\img\dino\lv3dino{self.img_num}.png')
        if(self.lv == 4):
            self.texture = pygame.image.load(f'assets\img\dino\lv4dino{self.img_num}.png')      
        
    def set_sound(self):
        
        """
        Chức năng: Phương thức này thiết lập âm thanh của đối tượng Dino.
    
        Input:
            Tệp âm thanh jump.wav
            
        Output:
            Load âm thanh jump.wav
        """
        
        self.sound = pygame.mixer.Sound('assets\sound\jump.wav')
        
    def jump(self):
        
        """
        Chức năng: Phương thức này đổi trạng thái của đối tượng Dino thành trạng thái nhảy và phát âm thanh nhảy.
        
        Input:
            sound: Dùng biến này để lấy âm thanh và phát
            jumping, running: Giá trị của 2 biến này là boolean và được lấy từ init
        
        Output:
            Trả về biến boolean định nghĩa trạng nhảy của đối tượng Dino
        """
        
        self.sound.play()
        self.jumping = True
        self.running = False
        
    def fall(self):
        
        """
        Chức năng: Phương thức này đổi trạng thái của đối tượng Dino thành trạng thái rơi.
        
        Input:
            falling, jumping: Giá trị của 2 biến này là boolean và được lấy từ init
        
        Output:
            Trả về biến boolean định nghĩa trạng rơi của đối tượng Dino
        """
        
        self.falling = True
        self.jumping = False
        
    def run(self):
        
        """
        Chức năng: Phương thức này đổi trạng thái của đối tượng Dino thành trạng thái chạy.
        
        Input:
            running, falling: Giá trị của 2 biến này là boolean và được lấy từ init
        
        Output:
            Trả về biến boolean định nghĩa trạng chạy của đối tượng Dino
        """
        
        self.running = True
        self.falling = False

# Tạo lớp chướng ngại vật
class Gun:
    
    """
    Chức năng: class này này khởi tạo đối tượng chướng ngại vật là hình viên đạn với chiều rộng là 113, chiều cao là 90, vị trí x là một đối số
    và vị trí y là 270. Thiết lập hình dạng của súng bằng phương thức 'set_texture()' và hiển thị nó trên màn hình bằng phương thức 'show()'.
    
    Args:
        x: Tọa độ x của viên đạn dùng để tạo vòng lặp.
    """
    
    def __init__(self, x):
        
        """
        Chức năng: Đây là phương thức khởi tạo của lớp Gun. Nó khởi tạo các thuộc tính của lớp như chiều rộng, chiều cao, 
        vị trí x, vị trí y và gọi phương thức set_texture() để đặt load hình ảnh viên đạn.
        
        Args:
            x: Vị trí x ban đầu của viên đạn trên màn hình.
            
        Return:
            None
        """
        
        self.width = 113
        self.height = 90
        self.x = x
        self.y = 270
        self.set_texture()
        self.show()
    
    def update(self, def_x):
        
        """
        Chức năng: Cập nhật vị trí x của viên đạn theo giá trị def_x.
        
        Args:
            def_x: Vị trí di chuyển của viên đạn.
            
        Returns:
            None
        """
        
        self.x += def_x
    
    def show(self):
        
        """
        Chức năng: Sử dụng phương thức blit() của module pygame để hiển thị đối tượng Surface của hình viên đạn lên màn hình tại tọa độ x và y.
        
        Attributes:
            x: Tọa độ x của hình nền.
            y: Tọa độ y của hình nền.
            texture (Surface): Đối tượng Surface tạo từ hình ảnh của hình nền.
        """
        
        screen.blit(self.texture, (self.x, self.y))
    
    def set_texture(self):
        
        """
        Chức năng: Phương thức này dùng để load hình ảnh chướng ngại vật hình viên đạn vào chương trình.
        
        Input:
            Hình ảnh gun.png
            
        Output:
            Hình ảnh chướng ngại vật hình viên đạn
        """
        
        self.texture = pygame.image.load(r'assets\img\obstacle\gun.png')

# Kiểm tra va chạm
class Collision:
    
    """
    Chức năng: class Collision dùng để xử lý va chạm giữa các đối tượng trong game.
    """
    
    def between(self, obj1, obj2):
        
        """
        Chức năng: Phương thức này tính khoảng cách giữa obj1 và obj2 sử dụng công thức khoảng cách và trả về giá trị boolean cho biết 
        khoảng cách có nhỏ hơn 30 hay không. Nếu khoảng cách nhỏ hơn 30 thì xảy ra va chạm.
        
        Input:
            obj1: Đối tượng khủng long.
            obj2: Đối tượng viên đạn.
            
        Output:
            bool: Trả về True nếu có va chạm, ngược lại trả về False.
        """
        
        distance = math.sqrt( (obj1.x - obj2.x)**2 + (obj1.y - obj2.y)**2 )
        return distance < 30

# Tạo lớp điểm số
class Score:
    
    """
    Chức năng: Class Score quản lý việc hiển thị điểm số và điểm cao nhất trong game.
    """
    
    def __init__(self, hscore):
        
        """
        Chức năng: Phương thức khởi tạo của lớp Score. Nó khởi tạo các thuộc tính của lớp như điểm số, điểm cao nhất,
        font để hiển thị điểm số, font để hiển thị điểm cao nhất và màu chữ, và gọi phương thức 'set_sound()' 
        để khởi tạo nhạc và phát khi điểm số tăng.
        
        Args:
            hscore (int): Lưu trữ biến điểm cao nhất và hiển thị lại những vòng chơi tiếp theo."
        """
        
        self.score = 0
        self.hscore = hscore
        self.font_score = pygame.font.SysFont('monospace', 38, bold=True)
        self.font_hscore = pygame.font.SysFont('monospace', 20)
        self.color = (0, 0, 0)
        self.set_sound()
        self.show()
        
    def update(self, loop):
        
        """
        Chức năng: Phương thức này cập nhật điểm mỗi 10 vòng lặp và kiểm tra xem điểm hiện tại có phải là điểm cao nhất hiện tại không.
        Nó phát ra một âm thanh mỗi 50 điểm.

        Args:
        loop (int): Số vòng lặp hiện tại.

        Output: Giá trị của loop
        """
        
        self.score = loop // 10
        self.check_hscore()
        self.check_sound()
        
    def set_sound(self):
        
        """
        Chức năng: Phương thức này dùng để load âm thanh khi nhân vật đạt mỗi 50 điểm.
        
        Input:
            File âm thanh point.wav
            
        Output:
            Âm thanh khi đạt mỗi 50 điểm
        """
        
        self.sound = pygame.mixer.Sound('assets\sound\point.wav')
        
    def check_hscore(self):
        
        """
        Chức năng: Phương thức này kiểm tra xem điểm hiện tại có phải là điểm cao nhất hiện tại không.

        Output: high score hiện tại
        """
        
        if self.score >= self.hscore:
            self.hscore = self.score
            
    def check_sound(self):
        
        """
        Chức năng: Hàm này dùng để kiểm tra xem điểm hiện tại đạt mỗi 50 thì nó phát âm thanh.
        
        Output:
            sound: Âm thanh đã load ở hàm set_sound
        """
        
        if self.score % 50 == 0 and self.score != 0:
            self.sound.play()
    
    def show(self):
        
        """
        Chức năng: Phương thức này hiển thị điểm cao nhất và điểm hiện tại trên màn hình bằng cách sử dụng phương thức render() của module pygame.
        
        Input: None
        
        Output:
            label1: Là điểm số cao nhất hiển thị ở góc phải trên cùng màn hình
            label2:Là điểm số hiện tại hiển thị ở giữa màn hình
        """
        
        self.label1 = self.font_hscore.render(f'High Score: {self.hscore}' , True, self.color)
        self.label2 = self.font_score.render(f'{self.score}m', True, self.color)
        lable_width = self.label1.get_rect().width
        screen.blit(self.label1, (WIDTH - lable_width - 10, 10))
        screen.blit(self.label2, (WIDTH // 2 - 35, 70))

# Tạo lớp trò chơi    
class Game:
        
    def __init__(self, hscore = 0):
        
        """
        Chức năng: khởi tạo các thuộc tính của game, như: mảng đối tượng background, đối tượng nhân vật, các đối tượng vật cản, 
        đối tượng xử lý va chạm, đối tượng hiển thị điểm số, trạng thái của game (đang chơi hay game over), tốc độ của game, đối tượng 
        âm thanh, và các đối tượng label.

        Input:
            hscore (int, optional): Điểm số lớn nhất mà người chơi đã đạt được trong game (mặc định là 0).
        """
        
        self.bg = [BG(0), BG(WIDTH)]
        self.dino = Dino()
        self.obstacle = []
        self.collision = Collision()
        self.score = Score(hscore)
        self.playing = False
        self.speed = 5
        self.appear_gun()
        self.set_sound()
        self.set_labels()
        
    def set_sound(self):
        
        """
        Chức năng: Load âm thanh
        """
        
        self.sound = pygame.mixer.Sound('assets\sound\die.wav')
        
    def set_labels(self):
        
        """
        Chức năng: Tạo font chữ cho các tiêu đề khi game over và hiển thị bằng phương thức blit()
        """
        
        big_font = pygame.font.SysFont('monospace', 38, bold=True)
        small_font = pygame.font.SysFont('monospace', 28)
        self.big_label = big_font.render(f'G A M E  O V E R', True, (0, 0, 0))
        self.small_label = small_font.render(f'Nhấn phím ENTER để bắt đầu lại', True, (0, 0, 0))
        
    def start(self):
        
        """
        Chức năng: Khởi tạo lại giá trị playing
        
        Input:
            playing: Là biến nhận giá trị boolean để xác định game đang chạy hay game over
            
        Output: Giá trị boolean
        """
        
        self.playing = True
        
    def end(self):
        
        """
        Chức năng: Hiển thị màn hình game over và ngừng chơi, đồng thời phát âm thanh khi nhân vật va chạm với vật cản
        """
        
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
        
        """
        Chức năng: Xác định xem có hiển thị viên đạn mới trong game hay không.
        Input:
            loop: số lần lặp hiện tại trong game
            
        Output: Trả về True nếu loop chia hết cho 100, ngược lại trả về False.
        """
        
        return loop % 100 == 0 # Xuất hiện khi con số chia hết cho 100 (Tránh dồn dập)
    
    def appear_gun(self):
        
        """
        Style: Hàm xử lý chức năng
        Chức năng: Hàm này dùng để tạo ra viên đạn mới và thêm nó vào mảng self.obstacle
        
        Nếu mảng self.obstacle không rỗng thì lấy vị trí viên đạn cuối cùng và tạo ra viên đạn mới có vị trí ngẫu nhiên trong khoảng: 
        x = vị trí viên đạn cuối cùng + chiều rộng của con Dino + 155
        y = chiều rộng của màn hình + vị trí viên đạn cuối cùng + chiều rộng của con Dino + 155
        
        Nếu mảng self.obstacle rỗng thì tạo ra viên đạn mới có vị trí ngẫu nhiên trong khoảng: 
        x = Chiều rộng của màn hình + 300
        y = 1200
        """
        
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
        """
        Chức năng: Hàm dùng để kiểm tra điểm hiện tại có lớn hơn 50 và nhỏ hơn hoặc bằng 100 hay không. Nếu đúng, hàm sẽ trả về 
        giá trị True, ngược lại sẽ trả về False. Nếu True, nhân vật sẽ biến đổi thành đối tượng nhân vật kế tiếp.
        
        Input: None
        
        Output: Giá trị boolean
        """
        
        if self.score.score > 50 and self.score.score <= 100:
            return True
        
    def Uplv2(self):

        """
        Chức năng: Tương tự hàm Uplv1()
        """
        
        if self.score.score > 100 and self.score.score <= 150:
            return True
        
    def Uplv3(self):

        """
        Chức năng: Tương tự hàm Uplv1()
        """
        
        if self.score.score > 150 and self.score.score <= 200:
            return True
        
    def Uplv4(self):

        """
        Chức năng: Tương tự hàm Uplv1()
        """
        
        if self.score.score > 200:
            return True

    def restart(self):
        
        """
        Chức năng: Khởi tạo lại trạng thái ban đầu của trò chơi, trong đó giá trị điểm cao nhất (high score) lưu lại và 
        truyền vào trong lần chơi kế tiếp.

        Input: None

        Output: Trạng thái ban đầu của trò chơi được khởi tạo lại.
        """
        
        self.__init__(hscore = self.score.hscore)

# Vòng lặp chính của game
def main():
    
    """
    Chức năng: Phương pháp này là vòng lặp chính của trò chơi nơi tất cả các đối tượng trò chơi được cập nhật và hiển thị trên màn hình. 
    Tốc độ trò chơi tăng lên sau mỗi 50 điểm. Vòng lặp sẽ kết thúc nếu người chơi va chạm với chướng ngại vật hoặc thoát khỏi trò chơi. 
    Người chơi cũng có thể khởi động lại trò chơi bằng cách nhấn phím Enter.
    """
    
    # Objects
    game = Game()
    dino = game.dino
    
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
                dino.lv = 1
                x += 0.02
                if x > 70:
                    x = 70
                #print('Giá trị FPS LV1: ',x)
                clock.tick(x)
                
            elif game.Uplv2():
                dino.lv = 2
                x += 0.02
                if x > 80:
                    x = 80
                #print('Giá trị FPS LV2: ',x)
                clock.tick(x)
                
            elif game.Uplv3():
                dino.lv = 3
                x += 0.02
                if x > 90:
                    x = 90
                print('Giá trị FPS LV3: ',x)
                clock.tick(x)
                
            elif game.Uplv4():
                dino.lv = 4
                x += 0.02
                print('Giá trị FPS LV4: ',x)
                clock.tick(x)
                
            else:
                x = 60
                #print('Giá trị FPS ban đầu: ',x)
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
    
    """
    Chức năng: Class để hiển thị màn hình bắt đầu với hình của 2 nhân vật chính là nhân vật Dino và chướng ngại vật gun và nhấp nháy 
    phông chữ "Nhấn phím bất kì để bắt đầu" để người chơi biết cách bắt đầu chơi trò chơi.

    Attributes:
        flash (bool): Trạng thái nhấp nháy của phông chữ.
        sound (pygame.mixer.Sound): Âm thanh bắt đầu khi khởi động game.
        texture (pygame.Surface): Hình nền.
    """
    
    def __init__(self):
        
        """
        Chức năng: Hàm này khởi tạo các thuộc tính của class Streen, bao gồm trạng thái nhấp nháy của phông chữ, âm thanh, 
        texture và hiển thị tiêu đề trên màn hình.
        """
        
        self.flash = True
        self.set_sound()
        self.set_texture()
        self.show()
        self.title()
        
    def set_sound(self):
        
        """
        Chức năng: Phương thức này dùng để load âm thanh khi khởi động trò chơi.
        
        Input:
            File âm thanh start.wav
            
        Output:
            Âm thanh khi khởi động trò chơi.
        """
        
        self.sound = pygame.mixer.Sound('assets\sound\start.wav')
        
    def title(self):
        
        """
        Chức năng: Phương thức này dùng để xử lý hiển thị của tiêu đề "Nhấn phím bất kì để bắt đầu". Sau mỗi chu kì 1 giây thì tiêu đề
        sẽ hiện sau đó ẩn và liên tục trong vòng lặp như vậy tạo nên sự sinh động cho trò chơi.
        
        Input: None
            
        Output: None
        """
        
        # Tính toán chu kỳ nhấp nháy của phông chữ, true là hiện, false là ẩn
        self.current_time = pygame.time.get_ticks()
        
        if self.current_time % 1000 < 500: # Chữ sẽ nhấp nháy theo chu kì mỗi 1s
            self.flash = True # Chữ hiện
        else:
            self.flash = False # Chữ ẩn

        # Hiển thị phông chữ theo trạng thái flash
        if self.flash:
            font = pygame.font.SysFont('monospace', 20, bold=True)
            self.text = font.render("Nhấn phím bất kì để bắt đầu", True, (0, 0, 0))
            screen.blit(self.text, (WIDTH // 2 - 140, HEIGHT // 2 + 120))
    
    def show(self):
        
        """
        Chức năng: Hiển thị màn hình khi khởi động game và tiếng âm đầu màn hình cùng với chuỗi nhấp nháy "Nhấn phím bất kì để bắt đầu"
        """
        
        screen.blit(self.texture, (0, 0))
        self.sound.play()
        self.title()

    def set_texture(self):
        
        """
        Chức năng: Phương thức này dùng để load hình ảnh màn hình bắt đầu vào chương trình.
        
        Input:
            Hình ảnh screen.png
            
        Output:
            Hình ảnh màn hình bắt đầu khi khởi động game
        """
        
        self.texture = pygame.image.load(r'assets\img\screen.png')

def menu():
    
    """
    Chức năng: Gọi hàm khởi tạo màn hình khi khởi động game. Khi người dùng nhấn phím, hàm này sẽ dừng âm thanh menu và 
    chuyển qua hàm main().
    """
    
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

