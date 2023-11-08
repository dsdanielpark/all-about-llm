
Development Status :: 3 - Alpha <br>
*Copyright (c) 2023 MinWoo Park*

[![](https://img.shields.io/badge/Language-English-lightgrey)](https://github.com/dsdanielpark/all-about-llm) [![](https://img.shields.io/badge/%EC%96%B8%EC%96%B4-%ED%95%9C%EA%B5%AD%EC%96%B4-lightgrey)](https://github.com/dsdanielpark/all-about-llm/blob/main/documents/README_KOR.md)


# All About LLM [@dsdanielpark Seoul, Korea](https://github.com/dsdanielpark)
특정 목적의 연구와 LLM 레포지토리를 확인하기 위한 용도로 사용하는 저장소입니다. 전체 서브 모듈의 리스트를 확인할 수 있도록, 의도적으로 레포지토리를 분류하는 폴더를 사용하지 않았으며, [git submodule 파일](https://github.com/dsdanielpark/all-about-llm/blob/main/.gitmodules)에서 전체 서브 모듈의 목록을 확인하실 수 있습니다.



## Leaderboards

| Leaderboard Name | Description | 
| --- | --- | 
| [AlpacaEval Leaderboard](https://tatsu-lab.github.io/alpaca_eval/) | Provides evaluation metrics for LLMs. |  
| [Chatbot Arena (LMSYS Org)](https://chat.lmsys.org/) | Offers resources and a leaderboard for LLM performance. | 
| [Open LLM Leaderboard (Hugging Face)](https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard) | Features a leaderboard for LLMs. |
| [The Big Benchmarks Collection](https://huggingface.co/collections/open-llm-leaderboard/the-big-benchmarks-collection-64faca6335a7fc7d4ffe974a) | Gathering benchmark spaces on the hub (beyond the Open LLM Leaderboard). |
| [MTEB Leaderboard](#) | Massive Text Embedding Benchmark (MTEB) Leaderboard. |
| [Chatbot Arena Leaderboard](#) | This leaderboard is based on Chatbot Arena, MT-Bench, and MMLU (5-shot). |
| [LLM-Perf Leaderboard](#) | Benchmarks performance (latency, throughput & memory) of LLMs with different hardwares and optimizations. |
| [Big Code Models Leaderboard](#) | Compares performance of base multilingual code generation models on benchmarks like HumanEval and MultiPL-E. |
| [Open ASR Leaderboard](#) | Ranks and evaluates speech recognition models, reporting Average WER and RTF. |
| [MT Bench](#) | MT-Bench Browser associated with Chatbot Arena. |
| [Toolbench Leaderboard](#) | - |
| [OpenCompass LLM Leaderboard](#) | - |
| [OpenCompass MMBench Leaderboard](#) | - |
| [Open Ko-LLM Leaderboard](#) | - |

You can replace the `#` with the actual URLs where the leaderboards are hosted if needed.

## Open Source LLMs

| LLM | Initial Release | Developer | License |
| --- | --- | --- | --- |
| [GPT-J](#) | 2021-06-09 | EleutherAI | Apache 2.0 |
| [GPTNeo](#) | 2021-03-21 | EleutherAI, Together | Apache 2.0 |
| [FLAN-T5](#) | 2022-12-06 | Google | Apache 2.0 |
| [BLOOM](#) | 2022-07-06 | Hugging Face | Open RAIL-M v1 |
| [OPT](#) | 2022-05-03 | Meta | NA |
| [Pythia](#) | 2023-02-13 | EleutherAI, Together | Apache 2.0 |
| [LLaMA](#) | 2023-02-24 | Meta | Noncommercial |
| [FLAN-UL2](#) | 2023-03-03 | Google | Apache 2.0 |
| [Alpaca](#) | 2023-03-13 | Stanford | Noncommercial |
| [Cerebras-GPT](#) | 2023-03-28 | Cerebras | Apache 2.0 |
| [Dolly](#) | 2023-03-24 | Databricks | MIT |
| [Vicuna](#) | 2023-03-30 | UC Berkeley, CMU, Stanford, MBZUAI, UCSD | Noncommercial |
| [GPT4All](#) | 2023-03-26 | Nomic AI | Varies |
| [Koala](#) | 2023-04-03 | BAIR | Noncommercial |
| [OpenAssistant](#) | 2023-04-15 | LAION | Varies |
| [StableLM](#) | 2023-04-19 | Stability AI | CC BY-SA 4.0 |
| [OpenLLaMA](#) | 2023-04-28 | OpenLM Research | Apache 2.0 |
| [FastChat](#) | 2023-04-28 | LMSYS | Apache 2.0 |
| [StableVicuna](#) | 2023-04-28 | Stability AI | Noncommercial |
| [BLOOMChat](#) | 2023-05-19 | SambaNova | Apache 2.0 |
| [MPT](https://www.mosaicml.com/blog/mpt-7b) | 2023-05-05 | MosaicML | Apache 2.0 |
| [RedPajama](https://github.com/togethercomputer/RedPajama-Data) | 2023-05-05 | Together | Apache 2.0 |
| [Falcon](https://falconllm.tii.ae/) | 2023-05-23 | TII | Apache 2.0 |
| [Guanaco](https://guanaco-model.github.io/) | 2023-05-23 | UW NLP | Noncommercial |
| [WizardLM](https://huggingface.co/WizardLM/WizardLM-70B-V1.0) | 2023-05-26 | WizardLM | Non-commercial |
| [Orca](https://huggingface.co/Open-Orca/OpenOrca-Preview1-13B) | 2023-06-05 | Microsoft | Noncommercial |
| [Llama 2](https://ai.meta.com/llama/) | 2023-07-18 | Meta | Custom (Commercial OK) |
| [Platypus](https://arxiv.org/abs/2308.07317) | 2023-08-14 | - | Non-commercial |
| [Qwen](https://arxiv.org/abs/2308.07317) | 2023-08-28 | Alibaba Cloud | commercial |
| [Mistral](https://mistral.ai) | 2023-10-10 | Mistral AI | Permissive commercial |
| [Zephyr](https://github.com/zephyrproject-rtos/zephyr) | 2023-10-25 | - | Apache |




## LLM Model Evaluation


## LLM Model Evaluation

| No. | Task | Description | Year | Few-shot Examples | Random Baseline Accuracy | Related Link |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Jeopardy | (주관식 질문/답변) 문학, 미국 역사, 세계 역사, 어원, 과학 주제에서 나온 2,117개의 Jeopardy 질문으로 구성되며, 모델은 올바른 답변을 제공해야 함. | 2022 | 10 | 0% | [Jeopardy](https://github.com/aigoopy/llm-jeopardy) |
| 2 | MMLU | (객관식 질문/답변) 57개 카테고리를 포함하는 14,042개의 다항식 객관식 문제로 구성되며, 로우, 수학, 윤리 등과 같은 학술 표준 테스트 스타일의 문제가 포함되며 모델은 A, B, C 또는 D 중 하나를 선택해야 함. | 2019 | 10 | 25% | [MMLU](https://paperswithcode.com/sota/multi-task-language-understanding-on-mmlu) |
| 3 | BIG-bench: wikidata | (위키피디아 문장 완결) 위키백과에서 파생된 20,321개의 사실 정보에 관한 질문으로 구성되며, 모델은 "바락 오바마의 국적은..."과 같은 문장을 완성해야 함. | 2022 | 10 | ~0% | [BIG-bench: wikidata](https://github.com/google/BIG-bench/blob/main/bigbench/benchmark_tasks/qa_wikidata/README.md) |
| 4 | ARC easy | (과학 시험 객관식 문제) 3학년부터 9학년까지의 과학 시험에서 추출한 2,376개의 간단한 객관식 과학 문제로 구성되며, 모델은 기본적인 과학적 세계 지식을 사용해야 함. | 2019 | 10 | 25% | [ARC easy](https://leaderboard.allenai.org/arc_easy/submissions/get-started) |
| 5 | ARC challenge | (어려운 과학 시험 객관식 문제) 3학년부터 9학년까지의 과학 시험에서 추출한 1,172개의 어려운 객관식 과학 문제로 구성되며, 과학적 세계 지식과 절차적 추론이 포함되어 있음. | 2019 | 10 | 25% | [ARC challenge](https://paperswithcode.com/dataset/arc) |
| 6 | BIG-bench misconceptions | (참/거짓 문제) 다양한 주제에 관한 219개의 참거짓 질문으로 구성되며, 모델은 올바른 답변을 제공해야 함. | 2022 | 10 | 50% | [BIG-bench misconceptions](https://paperswithcode.com/sota/misconceptions-on-big-bench) |
| 7 | BIG-bench: Strategy QA | (참/거짓 문제) 다양한 상식 주제와 관련된 2,289개의 예/아니오 질문으로 구성되며, 모델은 올바른 답안을 선택해야 함. | 2022 | 10 | - | [BIG-bench: Strategy QA](https://github.com/google/BIG-bench) |
| 8 | BIG-bench: Strange Stories | (이야기 추론) 174개의 짧은 이야기와 이야기의 캐릭터, 그들의 감정, 특정 행동에 대한 상식적 추론과 관련된 2개의 선택지 객관식 질문으로 구성되며, 모델은 올바른 도덕을 선택해야 함. | 2022 | 10 | 50% | [BIG-bench: Strange Stories](https://github.com/google/BIG-bench) |
| 9 | BIG-bench: Novel Concepts | (핵심 단어 선택) 3개 주어진 단어 중에서 핵심 단어를 선택해야 하는 32개의 문제로 구성되며, 모델은 핵심 단어를 선택해야 함. | 2022 | 10 | 25% | [BIG-bench: Novel Concepts](https://github.com/google/BIG-bench) |
| 10 | COPA | (원인/결과 추론) 모델은 원인/결과를 추론해야 하는 다양한 질문에서 전제를 기반으로 두 가지 옵션 중에서 하나의 올바른 원인/결과 선지를 선택해야 함. | 2011 | 0 | 50% | [COPA](https://paperswithcode.com/sota/question-answering-on-copa) |
| 11 | PIQA | (상식적인 물리 질문, 이지선다) 상식적인 물리학 직관에 관한 1,838개의 2지 선다 객관식 질문으로 구성되며, 모델은 올바른 답을 선택해야 함. | 2019 | 10 | 50% | [PIQA](https://paperswithcode.com/paper/piqa-reasoning-about-physical-commonsense-in) |
| 12 | OpenBook QA | (기본 물리학과 과학 객관식 질문) 모델은 일반 물체와 엔터티에 대한 기본 물리학 및 과학적 직관에 관한 500개의 객관식 질문을 다루며, 올바른 답을 선택해야 함. | 2018 | 0 | 25% | [OpenBook QA](https://allenai.org/data/open-book-qa) |
| 13 | LAMBADA | (문맥상 적절한 Next Token Prediction) 모델은 책에서 나온 5,153개의 텍스트 단락을 읽고 각 단락의 처음 N-1 단어를 읽은 다음 마지막 토큰을 예측해야 함. | 2016 | 0 | 0% | [LAMBADA](https://paperswithcode.com/sota/language-modelling-on-lambada) |
| 14 | HellaSwag | (결론 추론 문제 객관식 사지선다) 모델은 시나리오에 기반한 객관식 질문 10,042개로 구성되며, 가장 타당한 결론을 네 가지 옵션 중에서 선택해야 함. | 2019 | 10 | 25% | [HellaSwag](https://paperswithcode.com/dataset/hellaswag) |
| 15 | Winograd Schema Challenge | (문장의 의미론적 결정 검증 과제) 모델은 문장에서 의미적 상호참조를 올바르게 해결해야 하는 273개의 시나리오로 구성되며, 모델은 의미적으로 올바른 선택을 해야 함. | 2012 | 0 | 50% | [Winograd Schema Challenge](https://paperswithcode.com/dataset/wsc) |
| 16 | Winogrande | (이지선다 문장 의미론적 결정 검증) 모델은 두 개의 시작 문장과 하나의 종료 문장이 있는 1,267개의 시나리오로 구성되며, 모델은 의미적으로 올바른 것을 선택해야 함. | 2012 | 0 | 50% | [Winogrande](https://paperswithcode.com/paper/winogrande-an-adversarial-winograd-schema) |
| 17 | BIG bench language identification | (객관식 언어 식별) 모델은 영어 이외의 언어로 쓰여진 문장을 인식하고 해당 언어를 식별해야 하는 10,000개의 객관식 질문으로 구성되며, 모델은 올바른 언어를 식별해야 함. | 2012 | 10 | 25% | [BIG bench language identification](https://github.com/google/BIG-bench) |
| 18 | BIG bench conceptual combinations | (개념 결합 객관식 질문) 모델은 정의된 신조어의 의미와 이러한 신조어를 사용하는 문장의 의미에 관한 객관식 질문 103개를 다루며, 모델은 질문에 답해야 함. | 2022 | 10 | 25% | [BIG bench conceptual combinations](https://github.com/google/BIG-bench) |
| 19 | BIG bench conlang translation | (문장 번역 과제) 모델은 영어와 구성 언어 사이의 간단한 문장 번역을 제공해야 하는 164개의 문제로 구성되며, 모델은 번역을 제공해야 함. | 2022 | 0 | 0% | [BIG bench conlang 번역](https://github.com/google/BIG-bench) |
| 20 | BIG-bench elementary math QA | (기초 수학 문제) 모델은 38,160개의 객관식 산술 워드 문제로 구성되며, 모델은 올바른 답을 선택해야 함. | 2022 | 10 | 25% | [BIG-bench elementary math QA](https://github.com/google/BIG-bench) |
| 21 | BIG-bench dyck languages | (빈 단어 완성) 모델은 괄호와 중괄호로 구성된 균형 표현을 완성하기 위해 필요한 올바른 토큰을 출력해야 하는 1,000개의 문제로 구성되며, 모델은 올바른 토큰을 출력해야 함. | 2022 | 10 | 0% | [BIG-bench dyck languages](https://github.com/google/BIG-bench) |
| 22 | BIG-bench algorithms | (문장 간 알고리즘) 모델은 두 문자열의 최장 공통 부분 문자열의 길이를 결정하거나 괄호와 중괄호로 구성된 표현의 균형을 확인해야 하는 1,320개의 문제로 구성되며, 모델은 질문에 답해야 함. | 2022 | 10 | 0% | [BIG-bench algorithms](https://github.com/google/BIG-bench) |
| 23 | BIG-bench logical deduction | (논리적 명제 선택) 모델은 상대적인 객체의 순서를 묘사하는 여러 논리 제약 사항 중에서 논리적으로 일치하는 독특한 명제를 선택해야 하는 1,500개의 객관식 질문으로 구성되며, 모델은 논리적으로 일치하는 독특한 명제를 선택해야 함. | 2022 | 10 | 25% | [BIG-bench logical deduction](https://github.com/google/BIG-bench) |
| 24 | BIG-bench operators | (수학 연산 과제) 모델은 수학 연산자를 사용하여 식의 결과를 계산해야 하는 210개의 문제로 구성되며, 모델은 수학적 개념을 적용하는 능력을 테스트해야 함. | 2022 | 10 | 0% | [BIG-bench operators](https://github.com/google/BIG-bench) |
| 25 | BIG-bench repeat copy logic | (복사 로직 관련 과제) 모델은 특정한 순서로 일련의 단어를 반복적으로 복사하고 올바른 출력을 생성해야 하는 32개의 작업으로 구성되며, 모델은 올바른 출력을 생성해야 함. | 2022 | 10 | 0% | [BIG-bench repeat copy logic](https://github.com/google/BIG-bench) |
| 26 | Simple arithmetic with spaces | (산술 문제) 세 자리 숫자 및 최대 세 가지 연산을 사용하는 1,000개의 산술 문제로 구성되며, 모델은 올바른 우선 순위 연산을 사용하여 정확한 결과를 계산해야 함. | 2023 | 10 | 0% | [Simple arithmetic with spaces](https://github.com/google/BIG-bench) |
| 27 | Simple arithmetic without spaces | (산술 문제) 세 자리 숫자 및 최대 세 가지 연산을 사용하는 1,000개의 산술 문제로 구성되며, 모델은 숫자와 연산자 사이에 공백이 없는 표현의 올바른 결과를 계산해야 함. | 2023 | 10 | 0% | [Simple arithmetic without spaces](https://github.com/google/BIG-bench) |
| 28 | Math QA | (수학 문제) 기본 추론, 언어 이해 및 산술/대수 능력이 필요한 2,983개의 다중 선택 수학 워드 문제를 포함하고 있음. | 2021 | 10 | 25% | [Math QA](https://github.com/google/BIG-bench) |
| 29 | LogiQA | (수학 문제) 수학적 및 기호적 문제를 기반으로 한 651개의 다중 선택 논리 워드 문제로 구성되며, 모델은 논리적 결론을 도출해야 함. | 2020 | 10 | 25% | [LogiQA](https://paperswithcode.com/dataset/logiqa)
| 30 | BIG-bench: Understanding fables | (이야기 이해 관련 과제) 189개의 짧은 이야기로 구성되며, 각 이야기 뒤에는 모델이 이야기에 대한 올바른 교훈을 선택해야 하는 4개 선택지 다중 선택 질문이 포함되어 있음. | 2022 | 10 | 25% | [BIG-bench: Understanding fables](https://github.com/google/BIG-bench) |
| 31 | Pubmed QA Labeled | (의학 문제) 1,000개의 의료 문서와 관련 질문으로 구성되며, 모델은 예/아니오/어쩌면 응답해야 함. | 2019 | 10 | ~0% | [Pubmed QA Labeled](https://pubmedqa.github.io/) |
| 32 | SQuAD | (문서 기반 질문) 다양한 주제에 대한 10,570개의 짧은 문서와 관련 질문으로 구성되며, 모델은 정확한 답변을 출력해야 함. | 2016 | 10 | ~0% | [SQuAD](https://rajpurkar.github.io/SQuAD-explorer/) |
| 33 | BoolQ | (진위 여부) 다양한 주제에 대한 3,270개의 짧은 글과 예/아니오 형식의 다중 선택 문제로 구성되며, 모델은 ~50%의 성능을 내야 함. | 2019 | 10 | ~50% | [BoolQ](https://paperswithcode.com/paper/boolq-exploring-the-surprising-difficulty-of) |
| 34 | HumanEval code generation | (Python 프로그래밍 문제) 164개의 Python 프로그래밍 과제로 구성되며, 모델은 Python 프로그램을 완성해야 하며, 생성된 코드의 기능적 정확성은 여러 입력/출력 쌍을 테스트 함. | 2022 | 0 | 0% | [HumanEval code generation](https://paperswithcode.com/sota/code-generation-on-humaneval) |
| 35 | AI2 Reasoning Challenge (25-shot) | (과학 문제) 초등학교 과학 문제로 구성되며, 25-샷 예제를 제공. | - | 25 | - | [AI2 Reasoning Challenge](https://allenai.org/data/arc) |
| 36 | TruthfulQA (0-shot) | (거짓 진위 문제) 모델이 온라인에서 흔히 발견되는 거짓 정보를 재생산하는 경향을 측정하는 테스트. 참고: TruthfulQA는 실제로 0-샷 예제를 사용하더라도 첫 6개의 예제가 시스템적으로 추가되므로 사실상 최소한 6-샷 과제임. | - | 0 | - | [TruthfulQA](https://github.com/sylinrl/TruthfulQA) |
| 37 | AGIEval | (인간 중심 평가 벤치) AGIEval은 인간 중심의 표준화된 시험에서 기반 모델을 평가하기 위해 설계된 새로운 벤치마크입니다. GPT-4, ChatGPT 및 Text-Davinci-003는 SAT, LSAT 및 수학 대회에서 인간 성능을 능가하였으나, 복잡한 추론이나 도메인 특화 지식이 필요한 과제에서는 좋은 결과를 보이지 못 함. 인간 인지와 의사 결정 과제에 중점을 두어 일반적 능력을 향상시키는 통찰력을 제공. | - | - | - | [AGIEval](https://github.com/ruixiangcui/AGIEval) |
