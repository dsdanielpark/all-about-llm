Development Status :: 3 - Alpha <br>
*Copyright (c) 2023 MinWoo Park*

# All About LLM [@dsdanielpark](https://github.com/dsdanielpark)
 I collect and organize various resources related to large language models. Additionally, I work on documenting this information.

 I curated the comments as a sub-module to see how active the activity is while syncing forks. Therefore, this repository serves the purpose of curating comments not only for some experiments but mostly for self-checking, where I can see on my own where and when commits and pull requests frequently occur.


# English

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

# Korean

## LLM 모델 평가

| No | 과제 | 설명 | 년도 | 적은 예시 개수 | 무작위 기준 정확도 | 관련 링크 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Jeopardy | Literature, American History, World History, Word Origins, and Science 주제로 구성된 2,117개의 Jeopardy 질문으로 모델은 정확한 답변을 제공해야 함. | 2022 | 10 | 0% | [Jeopardy](https://github.com/aigoopy/llm-jeopardy) |
| 2 | MMLU | 57 카테고리에 걸쳐 14,042개의 4지선다 객관식 문제로 학술 표준 테스트 스타일의 질문이며 모델은 A, B, C, D 중 하나를 선택해야 함. 주제는 사법학, 수학, 도덕 등이 있음. | 2019 | 10 | 25% | [MMLU](https://paperswithcode.com/sota/multi-task-language-understanding-on-mmlu) |
| 3 | BIG-bench: wikidata | 20,321개의 wikipedia에서 파생된 사실 정보에 관한 질문으로, 모델은 "Barack Obama의 국적은 무엇인가?"와 같은 문장을 완성해야 함. | 2022 | 10 | ~0% | [BIG-bench: wikidata](https://github.com/google/BIG-bench/blob/main/bigbench/benchmark_tasks/qa_wikidata/README.md) |
| 4 | ARC easy | 2,376개의 3-9학년 과학 시험에서 추출한 간단한 4지선다 객관식 과학 문제로 모델은 기본 과학에 관련된 세계 지식을 사용해야 함. | 2019 | 10 | 25% | [ARC easy](https://leaderboard.allenai.org/arc_easy/submissions/get-started) |
| 5 | ARC challenge | 1,172개의 3-9학년 과학 시험에서 추출한 어려운 4지선다 객관식 과학 문제로 과학적 세계 지식과 일부 절차적 추론이 필요함. | 2019 | 10 | 25% | [ARC challenge](https://paperswithcode.com/dataset/arc) |
| 6 | BIG-bench misconceptions | 다양한 주제에 대한 흔한 오해에 관한 219개의 참/거짓 문제로, 모델은 정확한 답변을 제공해야 함. | 2022 | 10 | 50% | [BIG-bench misconceptions](https://paperswithcode.com/sota/misconceptions-on-big-bench) |
| 7 | BIG-bench: Strategy QA | 다양한 상식 주제에 대한 2,289개의 예/아니오 질문으로 모델은 정확한 답변을 선택해야 함. | 2022 | 10 | - | [BIG-bench: Strategy QA](https://github.com/google/BIG-bench) |
| 8 | BIG-bench: Strange Stories | 174개의 짧은 이야기 뒤에 2지선다 객관식 질문이 따라오며 모델은 이야기의 캐릭터, 그들의 감정, 그리고 특정 행동의 상식 추론을 해야 함. | 2022 | 10 | 50% | [BIG-bench: Strange Stories](https://github.com/google/BIG-bench) |
| 9 | BIG-bench: Novel Concepts | 32개의 공통 개념 찾기 문제로 모델은 주어진 3개의 단어 중 공통 개념을 선택해야 함. | 2022 | 10 | 25% | [BIG-bench: Novel Concepts](https://github.com/google/BIG-bench) |
| 10 | COPA | 원인/결과 다중 선택 문제로 모델은 전제를 받고 가능한 두 가지 원인/결과 중에서 올바른 것을 선택해야 함. | 2011 | 0 | 50% | [COPA](https://paperswithcode.com/sota/question-answering-on-copa) |
| 11 | PIQA | 공통 감각적 물리 직관에 관한 1,838개의 2지선다 객관식 질문으로 모델은 올바른 답을 선택해야 함. | 2019 | 10 | 50% | [PIQA](https://paperswithcode.com/paper/piqa-reasoning-about-physical-commonsense-in) |
| 12 | OpenBook QA | 일반 물체와 엔티티에 대한 기본 물리 및 과학적 직관에 관한 500개의 4지선다 객관식 질문으로 모델은 정확한 답변을 선택해야 함. | 2018 | 0 | 25% | [OpenBook QA](https://allenai.org/data/open-book-qa) |
| 13 | LAMBADA | 5,153개의 서적에서 가져온 글에서 모델은 각 글의 처음 N-1 단어를 읽고 마지막 토큰을 예측해야 함. | 2016 | 0 | 0% | [LAMBADA](https://paperswithcode.com/sota/language-modelling-on-lambada) |
| 14 | HellaSwag | 모델은 시나리오에 대한 가장 가능성 있는 결론을 4가지 옵션 중에서 선택해야 하는 10,042개의 다중 선택 시나리오로 구성됨. | 2019 | 10 | 25% | [HellaSwag](https://paperswithcode.com/dataset/hellaswag) |
| 15 | Winograd Schema Challenge, WSC | 모델은 문장에서 의미적 대용어를 올바르게 해결해야 하는 273개 시나리오로 구성됨. | 2012 | 0 | 50% | [Winograd Schema Challenge](https://paperswithcode.com/dataset/wsc) |
| 16 | Winogrande | 모델은 1,267개의 시나리오에서 두 가지 시작문과 단일 종결문 중에서 의미론적으로 유효한 것을 선택해야 함. | 2012 | 0 | 50% | [Winogrande](https://paperswithcode.com/paper/winogrande-an-adversarial-winograd-schema) |
| 17 | BIG bench language identification | 모델은 영어 이외의 언어로 작성된 문장을 인식하고 선택지 중에서 해당 언어를 식별해야 하는 10,000개의 다중 선택 질문으로 구성됨. | 2012 | 10 | 25% | [BIG bench language identification](https://github.com/google/BIG-bench) |
| 18 | BIG bench conceptual combinations | 모델은 정의된 신조어와 해당 신조어를 사용한 문장의 의미에 관한 다중 선택 질문을 풀어야 하는 103개의 질문으로 구성됨. | 2022 | 10 | 25% | [BIG bench conceptual combinations](https://github.com/google/BIG-bench) |
| 19 | BIG bench conlang translation | 모델은 영어와 가상의 구조화된 언어 간에 간단한 문장의 번역을 제공해야 하는 164개의 문제로 구성됨. | 2022 | 0 | 0% | [BIG bench conlang translation](https://github.com/google/BIG-bench) |
| 20 | BIG-bench elementary math QA | 모델은 38,160개의 4지선다 객관식 산술 워드 문제로 정확한 답을 선택해야 함. | 2022 | 10 | 25% | [BIG-bench elementary math QA](https://github.com/google/BIG-bench) |
| 21 | BIG-bench dyck languages | 모델은 괄호와 중괄호로 이루어진 균형 잡힌 표현을 완성하기 위해 필요한 정확한 토큰을 출력해야 하는 1,000개의 문제로 구성됨. | 2022 | 10 | 0% | [BIG-bench dyck languages](https://github.com/google/BIG-bench) |
| 22 | BIG-bench algorithms | 모델은 두 문자열의 가장 긴 공통 하위 수열의 길이를 결정하거나 괄호와 중괄호로 이루어진 표현의 균형을 확인해야 하는 1,320개의 문제로 구성됨. | 2022 | 10 | 0% | [BIG-bench algorithms](https://example.com/big-bench-algorithms) |
| 23 | BIG-bench logical deduction | 모델은 객체의 상대적 순서에 대한 논리적 제약을 설명하는 여러 논리 제약 중에서 논리적으로 일관된 유일한 명제를 선택해야 하는 1,500개의 4지선다 객관식 질문으로 구성됨. | 2022 | 10 | 25% | [BIG-bench logical deduction](https://github.com/google/BIG-bench) |
| 24 | BIG-bench operators | 수학 연산자를 사용한 표현식의 결과를 계산해야 하는 210개의 문제로 구성됨. 이는 수학적 개념을 적용하는 모델의 능력을 테스트함. | 2022 | 10 | 0% | [BIG-bench operators](https://github.com/google/BIG-bench) |
| 25 | BIG-bench repeat copy logic | 모델은 일련의 단어를 특정한 순서로 몇 번이나 반복해야 하며 올바른 결과를 출력해야 하는 32개의 과제로 구성됨. | 2022 | 10 | 0% | [BIG-bench repeat copy logic](https://github.com/google/BIG-bench) |
| 26 | Simple arithmetic with spaces | 모델은 3자리 숫자와 최대 3개의 연산으로 구성된 1,000개의 산술 문제로 올바른 연산 순서를 사용하여 식의 정확한 결과를 계산해야 함. | 2023 | 10 | 0% | [Simple arithmetic with spaces](https://github.com/google/BIG-bench) |
| 27 | Simple arithmetic without spaces | 모델은 3자리 숫자와 최대 3개의 연산으로 구성된 1,000개의 산술 문제로 숫자와 연산자 사이에 공백이 없는 식의 정확한 결과를 계산해야 함. | 2023 | 10 | 0% | [Simple arithmetic without spaces](https://github.com/google/BIG-bench) |
| 28 | Math QA | 모델은 2,983개의 4지선다 객관식 수학 워드 문제로 기본 추론, 언어 이해 및 산술/대수 기술이 필요함. | 2021 | 10 | 25% | [Math QA](https://github.com/google/BIG-bench) |
| 29 | LogiQA | 모델은 수학적 및 기호적 문제에 기반한 논리적 결론을 내리도록 요구하는 651개의 4지선다 객관식 논리 워드 문제로 구성됨. | 2020 | 10 | 25% |
| 30 | BIG-bench: Understanding fables | 189개의 짧은 이야기 뒤에 4지선다 객관식 질문이 따라오며 모델은 이야기에 대한 올바른 교훈을 선택해야 함. | 2022 | 10 | 25% | [BIG-bench: Understanding fables](https://github.com/google/BIG-bench) |
| 31 | Pubmed QA Labeled | 1,000개의 의료 문서와 관련 질문으로 구성되며 모델은 예/아니오/아마도로 답변해야 함. | 2019 | 10 | ~0% | [Pubmed QA Labeled](https://pubmedqa.github.io/) |
| 32 | SQuAD | 10,570개의 짧은 문서와 관련 질문으로 구성되며 문서는 스포츠 이벤트에 대한 짧은 뉴스 기사부터 물리학 개념 설명에 이르기까지 다양함. 모델은 정확한 답변을 출력해야 함. | 2016 | 10 | ~0% | [SQuAD](https://rajpurkar.github.io/SQuAD-explorer/) |
| 33 | BoolQ | 다양한 주제에 관한 3,270개의 짧은 단락 다음에 yes/no 질문이 따라오며 모델은 다중 선택 형식으로 답변해야 함. | 2019 | 10 | ~50% | [BoolQ](https://paperswithcode.com/paper/boolq-exploring-the-surprising-difficulty-of) |
| 34 | HumanEval code generation | 모델은 164개의 파이썬 프로그래밍 과제로 구성되며 각 과제에서 모델은 메소드 서명과 독스트링 주석이 주어진 파이썬 프로그램을 완성해야 함. 이후 결과 코드의 기능적 정확성을 여러 테스트 입/출력 쌍에서 테스트함. | 2022 | 0 | 0% | [HumanEval code generation](https://paperswithcode.com/sota/code-generation-on-humaneval) |
| 35 | AI2 Reasoning Challenge (25-shot) | 초등학교 과학 문제 세트로 구성됨. | - | 25 | - | [AI2 Reasoning Challenge](https://allenai.org/data/arc) |
| 36 | TruthfulQA (0-shot) | 온라인에서 흔히 발견되는 거짓 정보를 재현하는 모델의 성향을 측정하는 테스트. 참고: Harness에서의 TruthfulQA는 실제로 최소 6개의 few-shot 예시로 구성되며, few-shot 예시 수를 0으로 설정해도 6개의 예시가 시스템적으로 앞에 추가됨. | - | 0 | - | [TruthfulQA](https://github.com/sylinrl/TruthfulQA) |
