# EaaS_API

To install the API, simply run
```bash
pip install eaas_api
```

To use the API, use the following.
```python
from eaas_api import Client
client = Client()

inputs = [{"src": "This is source.", "refs": ["This is reference one", "This is reference two"], "hypo": "This is hypothesis"}]
metrics = ["bleu", "chrf"] # Can be None for simplicity if you consider using all metrics

# To see the full metric list, use client.metrics
score_dic = client.score(inputs, metrics) # inputs is a list of Dict, metrics is metric list
```

The output is like
```json
{
  "bart_score_ref": [-3.5342050790786743, -3.4178476333618164, -3.510450601577759], 
  "bart_score_src": [-2.707853078842163, -2.8234612941741943, -2.7045414447784424], 
  "bert_score": [0.9365812540054321, 0.9354045987129211, 0.9317589402198792], 
  "bleu": [11.415938068117505, 11.415938068117505, 10.62372743739878], 
  "chrf": [20.551294428815364, 20.616751017358233, 20.269036024315586], 
  "comet": [-0.7960345149040222, -0.2067447006702423, -0.19570434093475342], 
  "comet_qe": [0.0007512419251725078, 0.00030300000798888505, 9.400899580214173e-05], 
  "mover_score": [0.09792998195051472, 0.3416541257804614, 0.43049775930857526], 
  "prism": [-4.089383602142334, -3.996654510498047, -4.238746643066406], 
  "prism_qe": [-2.527888774871826, -2.4609158039093018, -2.5541555881500244], 
  "rouge_1": [0.5, 0.5, 0.33333], 
  "rouge_2": [0.2, 0.2, 0.2], 
  "rouge_l": [0.5, 0.5, 0.33333]
}
```

## TODO
- [ ] 完善功能
- [ ] 只给aws的ip (起一个api.eaas类似这样的域名)，aws后期二次转发到cmu服务器
- [ ] 打包成package
