"""
PROJECT: REAL_HUMAN_BEING.exe
STATUS:  LITERALLY ME
MOOD:    STOIC
"""

import time
import random
import sys
import os

# 真正的车手不需要Hello
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "1"
import pygame

# 引入颜色库，为了那该死的霓虹氛围
from colorama import init, Fore, Back, Style
init(autoreset=True)

# 定义色板 (Synthwave Palette)
NEON_PINK = Fore.MAGENTA
NEON_CYAN = Fore.CYAN
TAIL_LIGHT = Fore.RED
ASPHALT = Fore.LIGHTBLACK_EX
RESET = Style.RESET_ALL

def resource_path(relative_path):
    """解决 exe 打包后的资源路径问题"""
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

class SigmaDriver:
    """
    Inherits from: None (A Sigma stands alone)
    """
    def __init__(self, music_file="nightcall.mp3"):
        # 角色属性面板
        self.identity = "Ryan Gosling"
        self.jacket = "Scorpion Satin Jacket"
        self.accessory = "Toothpick"
        self.personality = "Silent"
        self.occupation = "Stuntman by day, Gateway driver by night"
        
        # 装备检查
        self.music_file = resource_path(music_file)
        self._init_audio_system()

    def _init_audio_system(self):
        try:
            pygame.mixer.init()
            pygame.mixer.music.load(self.music_file)
            pygame.mixer.music.set_volume(0.5)
            pygame.mixer.music.play(-1) # 无限循环，像我的孤独一样
            self.vibe_check = True
        except:
            self.vibe_check = False # 没音乐也能开，车手心中有曲

    def _draw_car(self):
        """
        绘制 1973 Chevy Malibu
        使用 ANSI 颜色代码绘制红色尾灯
        """
        c = NEON_PINK   # 车身颜色
        l = TAIL_LIGHT  # 尾灯颜色
        w = NEON_CYAN   # 玻璃反光
        
        # 这是一个精细的字符画车屁股
        car_sprite = [
            f"       {c}_________{RESET}",
            f"      {c}/  {w}|___|{c}  \\{RESET}",
            f"     {c}|  {w}_     _  {c}|{RESET}",
            f"     {c}| {l}[=]{c}_____{l}[=]{c} |{RESET}  <-- Chevy Malibu",
            f"     {c}'-(o)---(o)-'{RESET}"
        ]
        return car_sprite

    def _get_sigma_quote(self):
        """生成我的台词"""
        quotes = [
            "I drive.",
            "(Stares silently)",
            "(Chews toothpick aggressively)",
            "You give me a time and a place.",
            "I give you a five minute window.",
            "Real human being.",
            "And a real hero.",
            "...(Synthwave intensifies)...",
            "I don't sit in.",
        ]
        return random.choice(quotes)

    def start_engine(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"{NEON_CYAN}SYSTEM:  INITIALIZING NIGHTCALL PROTOCOL...{RESET}")
        time.sleep(1)
        print(f"{NEON_PINK}JACKET:  SCORPION EMBROIDERY DETECTED.{RESET}")
        time.sleep(1)
        print(f"{TAIL_LIGHT}ENGINE:  V8 RUMBLING.{RESET}")
        time.sleep(1)
        
        # 倒计时
        print("\n")
        for i in range(3, 0, -1):
            sys.stdout.write(f"\r{TAIL_LIGHT}{'🔴 ' * i}{RESET}")
            sys.stdout.flush()
            time.sleep(0.6)
        print(f"\r{NEON_CYAN}🟢 GO.{RESET}")
        time.sleep(0.5)

    def drive(self):
        self.start_engine()
        
        distance = 0
        road_width = 30
        car_art = self._draw_car()
        
        try:
            while True:
                # 1. 每一帧都清屏 (虽然有点闪，但这是最简单的动画方式)
                # 这种闪烁感其实很有 80年代 CRT 显示器的复古感
                # 如果你想不闪，需要更高级的 curses 库，但那样就不够 pythonic 了
                os.system('cls' if os.name == 'nt' else 'clear')

                # 2. 绘制天空/远景
                print(f"{NEON_PINK}\n        >>> L O S   A N G E L E S   2 0 4 9 <<<\n{RESET}")
                
                # 3. 动态生成道路 (透视效果)
                # 随着距离增加，路灯(Street Lights) 会划过
                street_light_l = f"{NEON_CYAN}*{RESET}" if distance % 8 == 0 else " "
                street_light_r = f"{NEON_CYAN}*{RESET}" if distance % 8 == 4 else " " # 错开闪烁
                
                # 车道线动画
                dash = f"{NEON_PINK}|{RESET}" if distance % 2 == 0 else " "
                
                # 打印远处的路 (窄) 到近处的路 (宽)
                # 这里为了简化，我们只打印一段路，然后把车放在底部
                
                print(f"      {street_light_l}          {dash}          {street_light_r}")
                print(f"    {street_light_l}            {dash}            {street_light_r}")
                print(f"   {street_light_l}             {dash}             {street_light_r}")
                print(f"  {street_light_l}              {dash}              {street_light_r}")
                print(f" {street_light_l}               {dash}               {street_light_r}")
                print(f"{street_light_l}                {dash}                {street_light_r}")

                # 4. 把车打印在路中间
                for line in car_art:
                    print(f"          {line}")

                # 5. 仪表盘与台词
                print(f"\n{ASPHALT}============================================{RESET}")
                print(f"[ SPEED: {NEON_CYAN}88 MPH{RESET} ] [ RPM: {TAIL_LIGHT}4500{RESET} ] [ MOOD: {NEON_PINK}LONELY{RESET} ]")
                
                # 偶尔来一句
                if distance % 15 == 0:
                    quote = self._get_sigma_quote()
                    print(f"\n> {NEON_CYAN}{quote}{RESET}")
                else:
                    print("\n") # 保持高度一致

                # 循环控制
                distance += 1
                time.sleep(0.1) # 帧率控制

        except KeyboardInterrupt:
            print(f"\n{TAIL_LIGHT}>>> DRIVE ENDED. BUT I AM STILL HERE. <<<{RESET}")
            if self.vibe_check:
                pygame.mixer.music.fadeout(2000)
            time.sleep(2)

if __name__ == "__main__":
    # 哪怕没有音乐，我也要上路
    # Because that's what I do.
    me = SigmaDriver("nightcall.mp3")
    me.drive()