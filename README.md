# EaaS_API

## Documentation
Setup can be found [here](https://github.com/yyy-Apple/sphinxdoc-test/blob/master/sphinx.md). Documentation at https://expressai.github.io/EaaS_API_dev/. Some references for writing docs can refer to
- https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html#rst-primer
- https://sphinx-tutorial.readthedocs.io/step-1/

## Usage
To install the API, simply run
```bash
pip install eaas
```

To use the API, run the following.

```python
from eaas import Client
client = Client()

# To use this API for scoring, you need to format your input as list of dictionary. Each dictionary consists of `src` (string, optional), `refs` (list of string, optional) and `hypo` (string, required). `src` and `refs` are optional based on the metrics you want to use. Please do not conduct any preprocessing on `src`, `refs` or `hypo`, we expect normal-cased detokenized texts. All preprocessing steps are taken by the metrics. Below is a simple example.

inputs = [{"src": "This is the source.", 
           "refs": ["This is the reference one.", "This is the reference two."],
           "hypo": "This is the generated hypothesis."}]
metrics = ["bleu", "chrf"] # Can be None for simplicity if you consider using all metrics

score_dic = client.score(inputs, metrics) # inputs is a list of Dict, metrics is metric list
```



The output is like
```
{
  'bleu': [32.46679154750991],  # Sample-level scores. A list of scores one for each sample.
  'corpus_bleu': 32.46679154750991, # Corpus-level score.
  'chrf': [38.56890099861521],
  'corpus_chrf': 38.56890099861521
}
```
## Short-term TODO
- [ ] Write config.json, add backend support.

## Long-term TODO
- [ ] 完善功能
- [ ] 只给aws的ip (起一个api.eaas类似这样的域名)，aws后期二次转发到cmu服务器
- [ ] 打包成package
- [X] metric corpus-level指标计算; BLEU corpus-level的计算检查（是否其他metric也有类似的）；我们可能要设计下返回结果的json格式
- [ ] 我们弄个文档，总结每个指标的默认预处理方法，超参数使用，考虑是否预留个接口给用户设置
- [ ] Confidence interval计算功能
- [ ] Fine-grained analysis功能
- [ ] 优化API访问效率
