Development Status :: 3 - Alpha <br>
*Copyright (c) 2023 MinWoo Park*

[![](https://img.shields.io/badge/Language-English-lightgrey)](https://github.com/dsdanielpark/all-about-llm) [![](https://img.shields.io/badge/%EC%96%B8%EC%96%B4-%ED%95%9C%EA%B5%AD%EC%96%B4-lightgrey)](https://github.com/dsdanielpark/all-about-llm/blob/main/documents/README_KOR.md)


# All About LLM 
Cutrated by [@dsdanielpark Seoul, Korea](https://github.com/dsdanielpark)

 I curated the comments as a sub-module to see how active the activity is while syncing forks. Therefore, this repository serves the purpose of curating comments not only for some experiments but mostly for self-checking, where I can see on my own where and when commits and pull requests frequently occur. To allow for viewing a list of all submodules, I intentionally do not use folders for organizing the repository. Additionally, you can view the complete list in the [git submodule file.](https://github.com/dsdanielpark/all-about-llm/blob/main/.gitmodules)
 
This repository contains only some of the models required for research, so please refer to other repositories for detailed information and updates.


## How to use
```
$ git clone https://github.com/dsdanielpark/all-about-llm.git
$ cd all-about-llm
$ git submodule update --init --recursive
```

## Leaderboards

| Leaderboard Name | Description | 
| --- | --- | 
| [AlpacaEval Leaderboard](#) | Provides evaluation metrics for LLMs. |  
| [Chatbot Arena (LMSYS Org)](#) | Offers resources and a leaderboard for LLM performance. | 
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
| [MPT](#) | 2023-05-05 | MosaicML | Apache 2.0 |
| [RedPajama-INCITE](#) | 2023-05-05 | Together | Apache 2.0 |
| [Falcon](#) | 2023-05-23 | TII | Apache 2.0 |
| [Guanaco](#) | 2023-05-23 | UW NLP | Noncommercial |
| [WizardLM](#) | 2023-05-26 | WizardLM | Non-commercial |
| [Orca](#) | 2023-06-05 | Microsoft | Noncommercial |
| [Llama 2](#) | 2023-07-18 | Meta | Custom (Commercial OK) |
| [Platypus](https://arxiv.org/abs/2308.07317) | 2023-08-14 | - | Non-commercial |
| [Qwen](https://arxiv.org/abs/2308.07317) | 2023-08-28 | Alibaba Cloud | commercial |
| [Mistral](https://mistral.ai) | 2023-10-10 | Mistral AI | Permissive commercial |
| [Zephyr](https://github.com/zephyrproject-rtos/zephyr) | 2023-10-25 | - | Apache |




## LLM Model Evaluation


| No. | Task | Description | Year | Few-shot Examples | Random Baseline Accuracy |
| --- | --- | --- | --- | --- | --- |
| 1 | [Jeopardy](https://github.com/aigoopy/llm-jeopardy) | Consists of 2,117 Jeopardy questions from the topics of Literature, American History, World History, Word Origins, and Science, where the model is expected to provide correct answers. | 2022 | 10 | 0% |
| 2 | [MMLU](https://paperswithcode.com/sota/multi-task-language-understanding-on-mmlu) | Comprises 14,042 multiple-choice questions across 57 categories, with academic-standard test-style questions covering subjects like law, mathematics, ethics, and more. The model must choose between options A, B, C, or D. | 2019 | 10 | 25% |
| 3 | [BIG-bench: wikidata](https://github.com/google/BIG-bench/blob/main/bigbench/benchmark_tasks/qa_wikidata/README.md) | Consists of 20,321 questions regarding factual information derived from Wikipedia. The model is expected to complete sentences like "Barack Obama's nationality is..." | 2022 | 10 | ~0% |
| 4 | [ARC easy](https://leaderboard.allenai.org/arc_easy/submissions/get-started) | Comprises 2,376 simple multiple-choice science questions extracted from 3rd to 9th-grade science exams, requiring the model to use basic scientific world knowledge. | 2019 | 10 | 25% |
| 5 | [ARC challenge](https://paperswithcode.com/dataset/arc) | Contains 1,172 challenging multiple-choice science questions extracted from 3rd to 9th-grade science exams, involving scientific world knowledge and some procedural reasoning. | 2019 | 10 | 25% |
| 6 | [BIG-bench misconceptions](https://paperswithcode.com/sota/misconceptions-on-big-bench) | Comprises 219 true/false questions about common misconceptions across various topics, and the model is expected to provide correct answers. | 2022 | 10 | 50% |
| 7 | [BIG-bench: Strategy QA](https://github.com/google/BIG-bench) | Consists of 2,289 yes/no questions related to various common-sense topics, and the model is expected to select the correct answers. | 2022 | 10 | - |
| 8 | [BIG-bench: Strange Stories](https://github.com/google/BIG-bench) | Comprises 174 short stories followed by 2-choice multiple-choice questions regarding characters, their emotions, and common-sense inferences about specific actions. | 2022 | 10 | 50% |
| 9 | [BIG-bench: Novel Concepts](https://github.com/google/BIG-bench) | Contains 32 problems for finding common concepts, and the model is expected to choose the common concept among three given words. | 2022 | 10 | 25% |
| 10 | [COPA](https://paperswithcode.com/sota/question-answering-on-copa) | Involves cause/effect multiple-choice questions where the model receives premises and must select the correct cause/effect among two options. | 2011 | 0 | 50% |
| 11 | [PIQA](https://paperswithcode.com/paper/piqa-reasoning-about-physical-commonsense-in) | Comprises 1,838 2-choice multiple-choice questions about common-sense physics intuition, and the model is expected to select the correct answer. | 2019 | 10 | 50% |
| 12 | [OpenBook QA](https://allenai.org/data/open-book-qa) | Consists of 500 multiple-choice questions about basic physics and scientific intuition for general objects and entities, and the model is expected to select the correct answers. | 2018 | 0 | 25% |
| 13 | [LAMBADA](https://paperswithcode.com/sota/language-modelling-on-lambada) | Contains 5,153 text passages from books where the model reads the first N-1 words of each passage and predicts the last token. | 2016 | 0 | 0% |
| 14 | [HellaSwag](https://paperswithcode.com/dataset/hellaswag) | Consists of 10,042 multiple-choice scenario-based questions where the model must choose the most plausible conclusion among four options. | 2019 | 10 | 25% |
| 15 | [Winograd Schema Challenge](https://paperswithcode.com/dataset/wsc) | Contains 273 scenarios where the model must correctly resolve semantic coreferences in sentences. | 2012 | 0 | 50% |
| 16 | [Winogrande](https://paperswithcode.com/paper/winogrande-an-adversarial-winograd-schema) | Comprises 1,267 scenarios with two starting sentences and a single ending sentence, and the model must select the semantically correct one. | 2012 | 0 | 50% |
| 17 | [BIG bench language identification](https://github.com/google/BIG-bench) | Contains 10,000 multiple-choice questions where the model must recognize sentences written in languages other than English and identify the corresponding language. | 2012 | 10 | 25% |
| 18 | [BIG bench conceptual combinations](https://github.com/google/BIG-bench) | Comprises 103 questions where the model answers multiple-choice questions about the meaning of defined neologisms and sentences using these neologisms. | 2022 | 10 | 25% |
| 19 | [BIG bench conlang translation](https://github.com/google/BIG-bench) | Contains 164 problems where the model provides translations of simple sentences between English and a constructed language. | 2022 | 0 | 0% |
| 20 | [BIG-bench elementary math QA](https://github.com/google/BIG-bench) | Consists of 38,160 multiple-choice arithmetic word problems, and the model is expected to select the correct answer. | 2022 | 10 | 25% |
| 21 | [BIG-bench dyck languages](https://github.com/google/BIG-bench) | Involves 1,000 problems where the model must output the correct tokens required to complete a balanced expression of parentheses and curly braces. | 2022 | 10 | 0% |
| 22 | [BIG-bench algorithms](https://example.com/big-bench-algorithms) | Contains 1,320 problems where the model must determine the length of the longest common subsequence of two strings or check the balance of expressions consisting of parentheses and curly braces. | 2022 | 10 | 0% |
| 23 | [BIG-bench logical deduction](https://github.com/google/BIG-bench) | Comprises 1,500 multiple-choice questions requiring the model to select the logically consistent unique proposition among multiple logical constraints describing the relative order of objects. | 2022 | 10 | 25% |
| 24 | [BIG-bench operators](https://github.com/google/BIG-bench) | Contains 210 problems where the model must calculate the result of expressions using mathematical operators, testing the model's ability to apply mathematical concepts. | 2022 | 10 | 0% |
| 25 | [BIG-bench repeat copy logic](https://github.com/google/BIG-bench) | Comprises 32 tasks where the model must repeatedly copy a series of words in a specific order and produce the correct output. | 2022 | 10 | 0% |
| 26 | [Simple arithmetic with spaces](https://github.com/google/BIG-bench) | Contains 1,000 arithmetic problems with three-digit numbers and up to three operations, where the model must calculate the correct result using the right order of operations. | 2023 | 10 | 0% |
| 27 | [Simple arithmetic without spaces](https://github.com/google/BIG-bench) | Comprises 1,000 arithmetic problems with three-digit numbers and up to three operations, where the model must calculate the correct result of expressions with no spaces between numbers and operators. | 2023 | 10 | 0% |
| 28 | [Math QA](https://github.com/google/BIG-bench) | Contains 2,983 multiple-choice math word problems, requiring basic inference, language comprehension, and arithmetic/algebra skills. | 2021 | 10 | 25% |
| 29 | [LogiQA](https://github.com/google/BIG-bench) | Comprises 651 multiple-choice logic word problems based on mathematical and symbolic problems, where the model must make logical conclusions. | 2020 | 10 | 25% |
| 30 | [BIG-bench: Understanding fables](https://github.com/google/BIG-bench) | Consists of 189 short stories followed by 4-choice multiple-choice questions where the model must select the correct moral for the story. | 2022 | 10 | 25% |
| 31 | [Pubmed QA Labeled](https://pubmedqa.github.io/) | Comprises 1,000 hand-labeled medical documents and related questions, where the model must respond with yes/no/maybe. | 2019 | 10 | ~0% |
| 32 | [SQuAD](https://rajpurkar.github.io/SQuAD-explorer/) | Consists of 10,570 short documents followed by related questions on various topics, and the model is expected to output the exact correct answer. | 2016 | 10 | ~0% |
| 33 | [BoolQ](https://paperswithcode.com/paper/boolq-exploring-the-surprising-difficulty-of) | Contains 3,270 short passages on a diverse range of subjects followed by yes/no questions in multiple-choice format. | 2019 | 10 | ~50% |
| 34 | [HumanEval code generation](https://paperswithcode.com/sota/code-generation-on-humaneval) | Comprises 164 Python programming challenges where the model is presented with the method signature and docstring comment for a Python program and is expected to complete the program. The resulting code's functional correctness is tested on a number of input/output pairs. | 2022 | 0 | 0% |
| 35 | [AI2 Reasoning Challenge (25-shot)](https://allenai.org/data/arc) | Consists of grade-school science questions. | - | 25 | - |
| 36 | [TruthfulQA (0-shot)](https://github.com/sylinrl/TruthfulQA) | A test to measure a model's propensity to reproduce falsehoods commonly found online. Note: TruthfulQA in the Harness is actually a minima 6-shot task, as it is prepended by 6 examples systematically, even when launched using 0 for the number of few-shot examples. | - | 0 | - |
| 37 | [AGIEval](https://github.com/ruixiangcui/AGIEval) | AGIEval is a new benchmark designed to assess foundation models in human-centric
