
import os

for name in os.listdir(os.path.join('..', 'image')):
    if not name.startswith('airm2m_'):
        continue
    print("![产品手册%s](./image/%s)" % (name, name))