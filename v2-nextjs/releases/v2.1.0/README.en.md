# [2026-06-22] v2.1.0 Minor Release

[한국어](./README.md) | [English](./README.en.md) | [日本語](./README.ja.md) | [Español](./README.es.md) | [Português (Brasil)](./README.pt-BR.md)

v2.1.0 lets supported browsers open the web app like an installed app, credits the public project RorScore, and improves how the AI finds the reference documents that fit a coding question first.

## Summary

- In supported browsers such as Chrome and Edge, the web app can be opened like an installed app.
- The install feature has no offline storage, push notifications, or background sync, and does not store sensitive assessment data or AI responses separately on the device.
- For a coding question such as `DQ+`, the AI consults the relevant scoring input documents first.
- The public project RorScore is credited as a reference.

## Installation and data storage

The install feature does not change how the app stores data or how API keys are protected. The API key is used for the AI connection in encrypted form; the connection lasts at most 24 hours, and ending it also deletes the key.

The installed app is also used with an internet connection and does not store sensitive assessment data or AI responses offline.

This change does not affect calculation results. When the coding assistant receives a question such as "When should DQ+ be coded rather than DQo or DQv/+?", it consults the relevant scoring input documents before the interpretation documents.

## RorScore credit

The public project RorScore is credited as a reference.
