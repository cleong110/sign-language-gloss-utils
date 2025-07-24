# sign-language-gloss-utils
Useful utilities to deal with glosses from, e.g. ASL Citizen, Sem-Lex, ASL-Lex, etc.


# Usage
```
git clone https://github.com/cleong110/sign-language-gloss-utils.git 
cd sign-language-gloss-utils
conda create -n sign-language-gloss-utils python=3.13 pip
conda activate sign-language-gloss-utils
# make sure you're using the right pip with pip --version or which pip
python -m pip install -e .
# python -m pip install -e .[dev] # to also install pytest, etc
python -m spacy download en_core_web_sm

```



# Citations and Sources

ASL Lex 2.0
```
    Sevcikova Sehyr, Z., Caselli, N., Cohen-Goldberg, A. M., & Emmorey, K. (2021). The ASL-LEX 2.0 Project: A database of lexical and phonological properties for 2,723 signs in American Sign Language. Journal of Deaf Studies and Deaf Education. doi.org/10.1093/deafed/enaa038.
    Caselli, N., Sevcikova Sehyr, Z., Cohen-Goldberg, A. M., & Emmorey, K. (2017). ASL-LEX: A lexical database of American Sign Language. Behavior Research Methods, 49(2), 784-801. doi:10.3758/s13428-016-0742-0.
```

ASL Citizen
```
@article{desai2023asl,
  title={ASL Citizen: A Community-Sourced Dataset for Advancing Isolated Sign Language Recognition},
  author={Desai, Aashaka and Berger, Lauren and Minakov, Fyodor O and Milan, Vanessa and Singh, Chinmay and Pumphrey, Kriston and Ladner, Richard E and Daum{\'e} III, Hal and Lu, Alex X and Caselli, Naomi and Bragg, Danielle},
  journal={arXiv preprint arXiv:2304.05934},
  year={2023}
}
```

Sem-Lex
```
@inproceedings{Kezar_2023, series={ASSETS ’23},
   title={The Sem-Lex Benchmark: Modeling ASL Signs and their Phonemes},
   url={http://dx.doi.org/10.1145/3597638.3608408},
   DOI={10.1145/3597638.3608408},
   booktitle={The 25th International ACM SIGACCESS Conference on Computers and Accessibility},
   publisher={ACM},
   author={Kezar, Lee and Thomason, Jesse and Caselli, Naomi and Sehyr, Zed and Pontecorvo, Elana},
   year={2023},
   month=oct, pages={1–10},
   collection={ASSETS ’23} }
```

ASL Knowledge Graph

```
@misc{kezar2024americansignlanguageknowledge,
      title={The American Sign Language Knowledge Graph: Infusing ASL Models with Linguistic Knowledge}, 
      author={Lee Kezar and Nidhi Munikote and Zian Zeng and Zed Sehyr and Naomi Caselli and Jesse Thomason},
      year={2024},
      eprint={2411.03568},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2411.03568}, 
}
```
