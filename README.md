Intro
===
What is ilt?
---
https://github.com/NCHUSG/ilts

What is django?
---
https://www.djangoproject.com/

Usage
===
這是一個用Django撰寫的App 能方便你使用ilt api的工具

他的作法大概如下:

```

+-------------+          +------------+
| some_views  | redirect | ilt_client |
| need_iltLog | -------> | 'run' view |
+-------------+          +------------+
      ^                        |
      |   bring session        |
      |     named 'user_files' |
      +-------------------------

```

利用這樣的方法 來達到簡化OAuth的繁瑣步驟

Install
===
1. Add  to your django project
---

```bash
$ cd <path_to_your_djangoproject> # example: ~/mysite/
$ git submodule add https://github.com/NCHUSG/iltClient_django-ver..git ilt_client
```

2. Edit urls.py
---
ex: mysite/urls.py

```py
# mysite/urls.py

# ...
urlpatterns = patterns(
	# ...
	url(r'^ilt_client/', include('ilt_client.urls', namespace="ilt_client")),
	# ...
)

```

3. Edit config.py
---

```bash
$ cd <path_to_your_djangoproject>/ilt_client/
$ cp example.config.py config.py
```

更多的資訊請參照config.py內文註解

How to use?
===
只要在views.py做一些小更動即可

ex:

```py
# polls/views.py

# ...

from ilt_client.ilt_filter import need_iltlogin

@need_iltlogin
def test(request):
    return HttpResponse('Hello')


```

你想要有登入的地方加上need_iltlogin decorator即可

如此一來你的session裡便有名為user_files這個session了

詳細實作辦法 請看原始碼XD

What's more?
===

在`ilt_client/urls.py`裡有一項`show`被註解掉

可以把他反註解掉並去 localhost:8000/ilt_client/show/

來看看session裡的東西是什麼