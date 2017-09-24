# srobot

## install

```
pip3 install -U "celery[redis]"
pip3 install flower
js9 'j.clients.redis.start4core()'
```

## start

go in root of this repo
suggest to use tmux

```
# in tab a
cd /opt/code/github/jumpscale/srobot
celery -A tasks worker --loglevel=info
# in tab b (is for UI)
cd /opt/code/github/jumpscale/srobot
celery -A tasks flower --address=0.0.0.0 --port=5555 --broker=redis://localhost:6379
```

## to do test

```
cd /opt/code/github/jumpscale/srobot
python3 test.py
```

## to see UI from host if using our docker js9 approach

```
ssh -L 5555:localhost:5555 root@localhost -p 2222
```

## to see console UI

```
celery -A tasks events --broker=redis://localhost:6379
```


