**Today** 21.2.22

오늘 늦었지만 조금이라도 정리하고 자보려고 한다.

Python Matplotlib 복습 시작!

```python
# matplotlib 불러오기
from matplotlib import pyplot as plt
plt.plot(a,b)
plt.show()

# label 붙이기
plt.plot(a,b, label = 'Deshaun')
plt.plot(c,d, label = 'Aditya')
plt.plot(e,f, label = 'Mengfei')

# title 붙이기
plt.title("Officers' days and hours")

# y축 label 추가
ple.ylabel("Hours worked")
 
# legend display
plt.legend()
plt.show()

```


```python
# 주석달기
plt.text(2.5,80, "Missing June data")
plt.show()

# line색깔넣기
plt.plot(data["Year"], data["Phoenix Police Dept"], label = "Phoenix", color = "DarkCyan")

plt.plot(data["Year"], data["Los Angeles Police Dept"], label="Los Angeles", linestyle = ":")

plt.plot(data["Year"], data["Philadelphia Police Dept"], label="Philadelphia", marker = "s")

plt.legend()
plt.show()

```

**Tomorrow**

내일 matplotlib 복습 못한 부분 해야함

Python project 시도해보기
