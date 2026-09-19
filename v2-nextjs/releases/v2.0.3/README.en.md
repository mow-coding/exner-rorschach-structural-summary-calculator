# [2026-06-11] v2.0.3 Bug-fix Release

[한국어](./README.md) | [English](./README.en.md) | [日本語](./README.ja.md) | [Español](./README.es.md) | [Português (Brasil)](./README.pt-BR.md)

v2.0.3 fixes the slow opening of the reference document screen and AI connection errors. The screen layout, usage, and the scope of AI answers have not changed; the reference document screen now opens faster, and invalid AI connection details are handled safely.

## Summary

- The reference document screen opens faster.
- The existing addresses of the 1,015 public documents in five languages remain unchanged.
- Invalid or expired AI connection details are handled safely as a disconnected state instead of an error screen.
- The result of the AI connection status check is not stored separately.
- Web app security issues known at the time were resolved.

## Reference document screen

Up to v2.0.2, the first reference document screen could appear late depending on the connection speed.

The calculator, the Structural Summary results, and the AI conversation screen were not affected, and the content and links of the reference documents did not change. However, the first reference document screen could appear late depending on the connection speed.

## What changed

The reference document screen opens faster, and the existing public document addresses remain unchanged.

Invalid or expired AI connection details are handled as a disconnected state without showing an error screen. The result of the AI connection status check is not stored separately.

Web app security issues known at the time were resolved.
