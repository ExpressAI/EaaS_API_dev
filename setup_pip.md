# Setup for Pypi

```shell
python setup.py sdist bdist_wheel --universal
twine upload dist/* -r pypi
```
#### 注意
上传文件名重复可以这样：twine upload --skip-existing dist/*
#用户名: pfliu_nlp 密码：Liupfs38