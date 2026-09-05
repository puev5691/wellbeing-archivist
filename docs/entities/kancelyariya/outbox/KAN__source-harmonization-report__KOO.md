# КООРДИНАТОРУ: ревизия источников, инструкций и recovery-контура КАНЦЕЛЯРА

## Кратко

КАНЦЕЛЯР завершил пробную инициацию, проверил внешний recovery-контур, выявил дефект процедуры и провёл согласование управляющих источников и верхних инструкций проекта.

Требуемое действие КООРДИНАТОРА: рассмотреть кандидаты как единый пакет, проверить их место в активном наборе источников и вынести ОПЕРАТОРУ решение по утверждению/замене.

## Что подтверждено

1. Recovery-пакет КАНЦЕЛЯРИИ существует в GitHub:
   `puev5691/wellbeing-archivist/docs/entities/kancelyariya/recovery-current/`.
2. Прежний snapshot, initiation, manifest и `sha256sums.txt` присутствовали; контрольная сумма snapshot совпала с файлом, полученным новым чатом.
3. Выявлен системный дефект: процедура требовала загрузить snapshot, но не делала внешнюю проверку recovery-locator и контрольных сумм обязательным барьером успешной инициации.
4. Подготовлена исправленная recovery-редакция v1.2-candidate.
5. Проведена ревизия корпуса источников и подготовлены согласованные кандидаты новых редакций.
6. Отдельно переработана верхняя инструкция проекта, чтобы она задавала режим поведения и не дублировала профильные каноны.

## Кандидаты источников

Каталог GitHub:

`docs/entities/kancelyariya/candidates/source-harmonization-v2/`

В пакет входят:

- аудит корпуса источников;
- `source-loading-policy-v2-candidate.md`;
- `project-instructions-core-v2-candidate.md`;
- `entity-roles-short-v2-candidate.md`;
- `entity-state-preservation-and-recovery-canon-v1_2-candidate.md`;
- `file-work-canon-universal-v2_2-candidate.md`;
- `artifact-routing-canon-v03-candidate.md`;
- `engineering-task-filter-v1-candidate.md`;
- `blagopoluchie-concept-core-v02-candidate.md`;
- `priority-board-template-v2-candidate.md`.

## Кандидат верхней инструкции

Каталог GitHub:

`docs/entities/kancelyariya/candidates/project-instructions-v2/`

Файл:

`KAN__project-chat-instructions-v2-candidate__OPR.md`

## Важные решения, которые пока НЕ приняты

- кандидаты не заменяют утверждённые источники автоматически;
- старые `draft/proposed-amendments` не удаляются до решения ОПЕРАТОРА;
- новая recovery-процедура не считается действующим каноном до утверждения;
- пустой priority-board остаётся шаблоном, а не текущим состоянием проекта.

## Что требуется от КООРДИНАТОРА

1. Рассмотреть аудит и набор кандидатов как один цикл гармонизации.
2. Определить, какие кандидаты готовы к утверждению ОПЕРАТОРОМ.
3. После решения организовать замену активных источников и перевод поглощённых старых черновиков в legacy/archive.
4. Учесть новый критерий инициации: внешний locator + фактическое наличие recovery-пакета + проверка состава/версии/контрольных сумм.

## Статус маршрута

GitHub-публикация: `verified` — кандидатный пакет источников, версия верхних инструкций и обновлённый recovery-snapshot записаны и повторно прочитаны/проверены через GitHub.
Доставка в чат КООРДИНАТОРА: `upload_pending` — текущий интерфейс не предоставляет КАНЦЕЛЯРУ инструмент прямой записи в другой чат. Следующий шаг: ОПЕРАТОР загружает этот файл в чат КООРДИНАТОРА.

---

## Служебная карточка

document_type: report-to-coordinator
from_entity: KAN
to_entity: KOO
status: upload_pending
project_time: generated_without_trusted_project_time
expected_action: review_candidates_and_route_operator_decision
responsibility_boundary: сообщение фиксирует результаты текущего цикла; утверждение новых нормативных источников остаётся за ОПЕРАТОРОМ
