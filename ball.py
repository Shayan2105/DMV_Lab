import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import numpy as np
import sys

class BallGame:
    def __init__(self):
        self.fig, self.ax = plt.subplots(figsize=(8, 6))
        self.fig.canvas.manager.set_window_title("Controllable Ball - Matplotlib")
        self.width, self.height = 800, 600
        self.ball_radius = 25
        self.speed = 8
        self.ball_x = self.width / 2
        self.ball_y = self.height / 2
        self.pressed = set()
        self.ax.set_xlim(0, self.width)
        self.ax.set_ylim(0, self.height)
        self.ax.set_aspect('equal')
        self.ax.grid(True, alpha=0.3)
        self.ax.set_facecolor('#111111')
        self.fig.patch.set_facecolor('#1e1e1e')
        self.ball = Circle((self.ball_x, self.ball_y), self.ball_radius, facecolor='#ff4444', edgecolor='white', linewidth=3)
        self.ax.add_patch(self.ball)
        self.ax.set_title("Move the ball with Arrow Keys\nPress 'Q' to Quit", fontsize=12, color='white', pad=20)
        self.fig.canvas.mpl_connect('key_press_event', self.on_key_press)
        self.fig.canvas.mpl_connect('key_release_event', self.on_key_release)
        self.timer = self.fig.canvas.new_timer(interval=30)
        self.timer.add_callback(self.update)
        self.timer.start()
        plt.show()
        
    def on_key_press(self, event):
        if event.key in ['q', 'Q']:
            plt.close(self.fig)
            sys.exit(0)
        key = event.key.lower()
        if key in ['left', 'a']:
            self.pressed.add('left')
        elif key in ['right', 'd']:
            self.pressed.add('right')
        elif key in ['up', 'w']:
            self.pressed.add('up')
        elif key in ['down', 's']:
            self.pressed.add('down')
    
    def on_key_release(self, event):
        key = event.key.lower()
        if key in ['left', 'a']:
            self.pressed.discard('left')
        elif key in ['right', 'd']:
            self.pressed.discard('right')
        elif key in ['up', 'w']:
            self.pressed.discard('up')
        elif key in ['down', 's']:
            self.pressed.discard('down')
    
    def update(self):
        if 'left' in self.pressed:
            self.ball_x -= self.speed
        if 'right' in self.pressed:
            self.ball_x += self.speed
        if 'up' in self.pressed:
            self.ball_y += self.speed
        if 'down' in self.pressed:
            self.ball_y -= self.speed
        self.ball_x = max(self.ball_radius, min(self.width - self.ball_radius, self.ball_x))
        self.ball_y = max(self.ball_radius, min(self.height - self.ball_radius, self.ball_y))
        self.ball.set_center((self.ball_x, self.ball_y))
        self.fig.canvas.draw_idle()

if __name__ == "__main__":
    game = BallGame()