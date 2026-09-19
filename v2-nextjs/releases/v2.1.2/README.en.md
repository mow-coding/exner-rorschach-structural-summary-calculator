# [2026-06-28] v2.1.2 Bug-fix Release

[한국어](./README.md) | [English](./README.en.md) | [日本語](./README.ja.md) | [Español](./README.es.md) | [Português (Brasil)](./README.pt-BR.md)

v2.1.2 adjusts how the coding assistant and the interpretation assistant answer: they answer as much as needed, are not cut off midway, and stay within the clinician's area of judgment. Apart from a small alignment fix in the API key dialog, the screens are unchanged.

## Summary

- The coding and interpretation assistants now behave more consistently in answer length and presentation.
- The coding assistant states candidate codes and the boundary of what the clinician must review more clearly. Answers that could be mistaken for automatic row entry or automatic application are blocked, and when the evidence is insufficient it asks for more observations.
- The interpretation assistant's limits are strengthened so it does not settle diagnostic, treatment, or legal questions from a single index. For broad questions with too few Structural Summary values, it no longer invents missing indices and instead suggests an order in which to check them.
- In the API key dialog, the OpenAI model name and the key field are shown on one easy-to-read line.
