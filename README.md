Development Status :: 3 - Alpha <br>
*Copyright (c) 2023 MinWoo Park*

[![](https://img.shields.io/badge/Language-English-lightgrey)](https://github.com/dsdanielpark/kor-sharegpt-deepl-alpaca) [![](https://img.shields.io/badge/%EC%96%B8%EC%96%B4-%ED%95%9C%EA%B5%AD%EC%96%B4-lightgrey)](https://github.com/dsdanielpark/kor-sharegpt-deepl-alpaca/blob/main/documents/README_KOR.md)


# All About LLM [@dsdanielpark Seoul, Korea](https://github.com/dsdanielpark)
 I collect and organize various resources related to large language models. Additionally, I work on documenting this information.

 I curated the comments as a sub-module to see how active the activity is while syncing forks. Therefore, this repository serves the purpose of curating comments not only for some experiments but mostly for self-checking, where I can see on my own where and when commits and pull requests frequently occur.

Certainly, I have removed the "Instruct / RLHF" columns and adjusted the table to make it fit within the width of the markdown. Here is the modified table:

## Leaderboards

| Leaderboard Name | Description | Reference |
| --- | --- | --- |
| AlpacaEval Leaderboard | Provides evaluation metrics for LLMs. | [Link](#) |
| Chatbot Arena (LMSYS Org) | Offers resources and a leaderboard for LLM performance. | [Leaderboard](#) |
| Open LLM Leaderboard (Hugging Face) | Features a leaderboard for LLMs. | [Link](#) |

## Open Source LLMs

| LLM | Initial Release | Developer | License | Reference |
| --- | --- | --- | --- | --- |
| Alpaca | 2023-03-13 | Stanford | Noncommercial | [Link](#) |
| BLOOM | 2022-07-06 | Hugging Face | Open RAIL-M v1 | [Link](#) |
| BLOOMChat | 2023-05-19 | SambaNova | Apache 2.0 | [Link](#) |
| Cerebras-GPT | 2023-03-28 | Cerebras | Apache 2.0 | [Link](#) |
| Dolly | 2023-03-24 | Databricks | MIT | [Link](#) |
| Falcon | 2023-05-23 | TII | Apache 2.0 | [Link](#) |
| FastChat | 2023-04-28 | LMSYS | Apache 2.0 | [Link](#) |
| FLAN-T5 | 2022-12-06 | Google | Apache 2.0 | [Link](#) |
| FLAN-UL2 | 2023-03-03 | Google | Apache 2.0 | [Link](#) |
| GPT-J | 2021-06-09 | EleutherAI | Apache 2.0 | [Link](#) |
| GPT4All | 2023-03-26 | Nomic AI | Varies | [Link](#) |
| GPTNeo | 2021-03-21 | EleutherAI, Together | Apache 2.0 | [Link](#) |
| Guanaco | 2023-05-23 | UW NLP | Noncommercial | [Link](#) |
| Koala | 2023-04-03 | BAIR | Noncommercial | [Link](#) |
| LLaMA | 2023-02-24 | Meta | Noncommercial | [Link](#) |
| Llama 2 | 2023-07-18 | Meta | Custom (Commercial OK) | [Link](#) |
| MPT | 2023-05-05 | MosaicML | Apache 2.0 | [Link](#) |
| OpenAssistant | 2023-04-15 | LAION | Varies | [Link](#) |
| OpenLLaMA | 2023-04-28 | OpenLM Research | Apache 2.0 | [Link](#) |
| OPT | 2022-05-03 | Meta | NA | [Link](#) |
| Orca | 2023-06-05 | Microsoft | Noncommercial | [Link](#) |
| Pythia | 2023-02-13 | EleutherAI, Together | Apache 2.0 | [Link](#) |
| RedPajama-INCITE | 2023-05-05 | Together | Apache 2.0 | [Link](#) |
| StableLM | 2023-04-19 | Stability AI | CC BY-SA 4.0 | [Link](#) |
| StableVicuna | 2023-04-28 | Stability AI | Noncommercial | [Link](#) |
| Vicuna | 2023-03-30 | UC Berkeley, CMU, Stanford, MBZUAI, UCSD | Noncommercial | [Link](#) |
| WizardLM | 2023-05-26 | WizardLM | Non-commercial | [Link](#) |
| Platypus | 2023-08-14 | - | Non-commercial | [Link](https://arxiv.org/abs/2308.07317) |
| Qwen | 2023-08-28 | Alibaba Cloud | commercial | [Link](https://arxiv.org/abs/2308.07317) |
| Zephyr | 2023-08-28 | - | Apache | [Link](https://github.com/zephyrproject-rtos/zephyr/blob/main/LICENSE) |
| Mistral | 2023-08-28 | Mistral AI | Permissive commercial | [Link](https://mistral.ai) |




## LLM Model Evaluation

| No. | Task | Description | Year | Few-shot Examples | Random Baseline Accuracy | Related Link |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Jeopardy | Consists of 2,117 Jeopardy questions from the topics of Literature, American History, World History, Word Origins, and Science, where the model is expected to provide correct answers. | 2022 | 10 | 0% | [Jeopardy](https://github.com/aigoopy/llm-jeopardy) |
| 2 | MMLU | Comprises 14,042 multiple-choice questions across 57 categories, with academic-standard test-style questions covering subjects like law, mathematics, ethics, and more. The model must choose between options A, B, C, or D. | 2019 | 10 | 25% | [MMLU](https://paperswithcode.com/sota/multi-task-language-understanding-on-mmlu) |
| 3 | BIG-bench: wikidata | Consists of 20,321 questions regarding factual information derived from Wikipedia. The model is expected to complete sentences like "Barack Obama's nationality is..." | 2022 | 10 | ~0% | [BIG-bench: wikidata](https://github.com/google/BIG-bench/blob/main/bigbench/benchmark_tasks/qa_wikidata/README.md) |
| 4 | ARC easy | Comprises 2,376 simple multiple-choice science questions extracted from 3rd to 9th-grade science exams, requiring the model to use basic scientific world knowledge. | 2019 | 10 | 25% | [ARC easy](https://leaderboard.allenai.org/arc_easy/submissions/get-started) |
| 5 | ARC challenge | Contains 1,172 challenging multiple-choice science questions extracted from 3rd to 9th-grade science exams, involving scientific world knowledge and some procedural reasoning. | 2019 | 10 | 25% | [ARC challenge](https://paperswithcode.com/dataset/arc) |
| 6 | BIG-bench misconceptions | Comprises 219 true/false questions about common misconceptions across various topics, and the model is expected to provide correct answers. | 2022 | 10 | 50% | [BIG-bench misconceptions](https://paperswithcode.com/sota/misconceptions-on-big-bench) |
| 7 | BIG-bench: Strategy QA | Consists of 2,289 yes/no questions related to various common-sense topics, and the model is expected to select the correct answers. | 2022 | 10 | - | [BIG-bench: Strategy QA](https://github.com/google/BIG-bench) |
| 8 | BIG-bench: Strange Stories | Comprises 174 short stories followed by 2-choice multiple-choice questions regarding characters, their emotions, and common-sense inferences about specific actions. | 2022 | 10 | 50% | [BIG-bench: Strange Stories](https://github.com/google/BIG-bench) |
| 9 | BIG-bench: Novel Concepts | Contains 32 problems for finding common concepts, and the model is expected to choose the common concept among three given words. | 2022 | 10 | 25% | [BIG-bench: Novel Concepts](https://github.com/google/BIG-bench) |
| 10 | COPA | Involves cause/effect multiple-choice questions where the model receives premises and must select the correct cause/effect among two options. | 2011 | 0 | 50% | [COPA](https://paperswithcode.com/sota/question-answering-on-copa) |
| 11 | PIQA | Comprises 1,838 2-choice multiple-choice questions about common-sense physics intuition, and the model is expected to select the correct answer. | 2019 | 10 | 50% | [PIQA](https://paperswithcode.com/paper/piqa-reasoning-about-physical-commonsense-in) |
| 12 | OpenBook QA | Consists of 500 multiple-choice questions about basic physics and scientific intuition for general objects and entities, and the model is expected to select the correct answers. | 2018 | 0 | 25% | [OpenBook QA](https://allenai.org/data/open-book-qa) |
| 13 | LAMBADA | Contains 5,153 text passages from books where the model reads the first N-1 words of each passage and predicts the last token. | 2016 | 0 | 0% | [LAMBADA](https://paperswithcode.com/sota/language-modelling-on-lambada) |
| 14 | HellaSwag | Consists of 10,042 multiple-choice scenario-based questions where the model must choose the most plausible conclusion among four options. | 2019 | 10 | 25% | [HellaSwag](https://paperswithcode.com/dataset/hellaswag) |
| 15 | Winograd Schema Challenge, WSC | Contains 273 scenarios where the model must correctly resolve semantic coreferences in sentences. | 2012 | 0 | 50% | [Winograd Schema Challenge](https://paperswithcode.com/dataset/wsc) |
| 16 | Winogrande | Comprises 1,267 scenarios with two starting sentences and a single ending sentence, and the model must select the semantically correct one. | 2012 | 0 | 50% | [Winogrande](https://paperswithcode.com/paper/winogrande-an-adversarial-winograd-schema) |
| 17 | BIG bench language identification | Contains 10,000 multiple-choice questions where the model must recognize sentences written in languages other than English and identify the corresponding language. | 2012 | 10 | 25% | [BIG bench language identification](https://github.com/google/BIG-bench) |
| 18 | BIG bench conceptual combinations | Comprises 103 questions where the model answers multiple-choice questions about the meaning of defined neologisms and sentences using these neologisms. | 2022 | 10 | 25% | [BIG bench conceptual combinations](https://github.com/google/BIG-bench) |
| 19 | BIG bench conlang translation | Contains 164 problems where the model provides translations of simple sentences between English and a constructed language. | 2022 | 0 | 0% | [BIG bench conlang translation](https://github.com/google/BIG-bench) |
| 20 | BIG-bench elementary math QA | Consists of 38,160 multiple-choice arithmetic word problems, and the model is expected to select the correct answer. | 2022 | 10 | 25% | [BIG-bench elementary math QA](https://github.com/google/BIG-bench) |
| 21 | BIG-bench dyck languages | Involves 1,000 problems where the model must output the correct tokens required to complete a balanced expression of parentheses and curly braces. | 2022 | 10 | 0% | [BIG-bench dyck languages](https://github.com/google/BIG-bench) |
| 22 | BIG-bench algorithms | Contains 1,320 problems where the model must determine the length of the longest common subsequence of two strings or check the balance of expressions consisting of parentheses and curly braces. | 2022 | 10 | 0% | [BIG-bench algorithms](https://example.com/big-bench-algorithms) |
| 23 | BIG-bench logical deduction | Comprises 1,500 multiple-choice questions requiring the model to select the logically consistent unique proposition among multiple logical constraints describing the relative order of objects. | 2022 | 10 | 25% | [BIG-bench logical deduction](https://github.com/google/BIG-bench) |
| 24 | BIG-bench operators | Contains 210 problems where the model must calculate the result of expressions using mathematical operators, testing the model's ability to apply mathematical concepts. | 2022 | 10 | 0% | [BIG-bench operators](https://github.com/google/BIG-bench) |
| 25 | BIG-bench repeat copy logic | Comprises 32 tasks where the model must repeatedly copy a series of words in a specific order and produce the correct output. | 2022 | 10 | 0% | [BIG-bench repeat copy logic](https://github.com/google/BIG-bench) |
| 26 | Simple arithmetic with spaces | Contains 1,000 arithmetic problems with three-digit numbers and up to three operations, where the model must calculate the correct result using the right order of operations. | 2023 | 10 | 0% | [Simple arithmetic with spaces](https://github.com/google/BIG-bench) |
| 27 | Simple arithmetic without spaces | Comprises 1,000 arithmetic problems with three-digit numbers and up to three operations, where the model must calculate the correct result of expressions with no spaces between numbers and operators. | 2023 | 10 | 0% | [Simple arithmetic without spaces](https://github.com/google/BIG-bench) |
| 28 | Math QA | Contains 2,983 multiple-choice math word problems, requiring basic inference, language comprehension, and arithmetic/algebra skills. | 2021 | 10 | 25% | [Math QA](https://github.com/google/BIG-bench) |
| 29 | LogiQA | Comprises 651 multiple-choice logic word problems based on mathematical and symbolic problems, where the model must make logical conclusions. | 2020 | 10 | 25% |
| 30 | BIG-bench: Understanding fables | Consists of 189 short stories followed by 4-choice multiple-choice questions where the model must select the correct moral for the story. | 2022 | 10 | 25% | [BIG-bench: Understanding fables](https://github.com/google/BIG-bench) |
| 31 | Pubmed QA Labeled | Comprises 1,000 hand-labeled medical documents and related questions, where the model must respond with yes/no/maybe. | 2019 | 10 | ~0% | [Pubmed QA Labeled](https://pubmedqa.github.io/) |
| 32 | SQuAD | Consists of 10,570 short documents followed by related questions on various topics, and the model is expected to output the exact correct answer. | 2016 | 10 | ~0% | [SQuAD](https://rajpurkar.github.io/SQuAD-explorer/) |
| 33 | BoolQ | Contains 3,270 short passages on a diverse range of subjects followed by yes/no questions in multiple-choice format. | 2019 | 10 | ~50% | [BoolQ](https://paperswithcode.com/paper/boolq-exploring-the-surprising-difficulty-of) |
| 34 | HumanEval code generation | Comprises 164 Python programming challenges where the model is presented with the method signature and docstring comment for a Python program and is expected to complete the program. The resulting code's functional correctness is tested on a number of input/output pairs. | 2022 | 0 | 0% | [HumanEval code generation](https://paperswithcode.com/sota/code-generation-on-humaneval) |
| 35 | AI2 Reasoning Challenge (25-shot) | Consists of grade-school science questions. | - | 25 | - | [AI2 Reasoning Challenge](https://allenai.org/data/arc) |
| 36 | TruthfulQA (0-shot) | A test to measure a model's propensity to reproduce falsehoods commonly found online. Note: TruthfulQA in the Harness is actually a minima 6-shot task, as it is prepended by 6 examples systematically, even when launched using 0 for the number of few-shot examples. | - | 0 | - | [TruthfulQA](https://github.com/sylinrl/TruthfulQA) |
| 37 | AGIEval | AGIEval is a new benchmark designed to assess foundation models in human-centric standardized exams. GPT-4, ChatGPT, and Text-Davinci-003 perform impressively, exceeding human performance in SAT, LSAT, and math competitions. However, they struggle with tasks requiring complex reasoning or domain-specific knowledge. This benchmark provides insights into enhancing general capabilities by focusing on human cognition and decision-making tasks. . | - | - | - | [AGIEval](https://github.com/ruixiangcui/AGIEval) |
