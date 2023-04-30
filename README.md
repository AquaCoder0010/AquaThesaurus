# AquaThesaurus
Simple one header Library made to get synonyms and antonyms of words from thesarus.com

add the source .py file into your project and write the following line of code to get synonyms and antonyms of a given word

```python
from AquaThesaurus import AquaThesaurus

thesaurus = AquaThesaurus();
word = "happy";

similar_list = thesaurus.getAntonyms(word);
print(similar_list);
```


