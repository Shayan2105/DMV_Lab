import matplotlib.pyplot as plt
from matplotlib.patches import Circle
from matplotlib.animation import FuncAnimation
import sys

print("=" * 55)
print("Automatic Bouncing Ball - Matplotlib Animation")
print("=" * 55)

try:
    width = int(input("Enter window width (recommended: 800): "))
    height = int(input("Enter window height (recommended: 600): "))
    ball_color = input("Enter ball color (e.g. red, blue, #ff4444): ").strip()
    speed = int(input("Enter ball speed (recommended: 6-12): "))
except ValueError:
    print("Invalid input! Using defaults: 800x600, red, speed=8")
    width, height = 800, 600
    ball_color = "red"
    speed = 8

width = max(400, width)
height = max(300, height)
speed = max(3, min(speed, 25))
ball_radius = 30
fig, ax = plt.subplots(figsize=(width / 100, height / 100))
fig.canvas.manager.set_window_title(f"Bouncing Ball - {width}×{height}")
ax.set_xlim(0, width)
ax.set_ylim(0, height)
ax.set_aspect('equal')
ax.grid(True, linestyle='--', alpha=0.3, color='white')
ax.set_facecolor('#0a0a0a')
fig.patch.set_facecolor('#1e1e1e')

ball_x = width / 2
ball_y = height / 2
dx = speed
dy = speed
ball = Circle((ball_x, ball_y), ball_radius,
              facecolor=ball_color, edgecolor='white', linewidth=4)
ax.add_patch(ball)
ax.set_title(f"Automatic Bouncing Ball\n"
             f"Size: {width}×{height} | Color: {ball_color} | Speed: {speed}\n"
             f"Close the window to exit", 
             fontsize=12, color='white', pad=20)
def update(frame):
    global ball_x, ball_y, dx, dy
    
    # Move the ball
    ball_x += dx
    ball_y += dy
    if ball_x - ball_radius <= 0 or ball_x + ball_radius >= width:
        dx = -dx
    if ball_y - ball_radius <= 0 or ball_y + ball_radius >= height:
        dy = -dy
    ball.set_center((ball_x, ball_y))
    
    return ball,
ani = FuncAnimation(fig, update, interval=16, blit=True, cache_frame_data=False)

print("\nBouncing Ball started! Close the window to exit.\n")

plt.show()