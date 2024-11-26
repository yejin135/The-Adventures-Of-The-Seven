from js import document
import asyncio

# 간단한 키 이벤트 핸들러
def on_key_down(event):
    key = event.key
    output = document.getElementById("output")
    if key == "ArrowUp":
        output.innerHTML = "You pressed UP!"
    elif key == "ArrowDown":
        output.innerHTML = "You pressed DOWN!"
    elif key == "ArrowLeft":
        output.innerHTML = "You pressed LEFT!"
    elif key == "ArrowRight":
        output.innerHTML = "You pressed RIGHT!"
    else:
        output.innerHTML = f"You pressed {key}!"

# HTML에 표시할 기본 텍스트 설정
output = document.createElement("div")
output.setAttribute("id", "output")
output.innerHTML = "Press any arrow key to start!"
document.body.appendChild(output)

# 이벤트 리스너 추가
document.addEventListener("keydown", on_key_down)
