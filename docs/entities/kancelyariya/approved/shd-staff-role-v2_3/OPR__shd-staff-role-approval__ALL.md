# Решение ОПЕРАТОРА: штатная интеграция SHD и role-source v2.3

## Решение

ОПЕРАТОР явно распорядился:
- перевести существующую Сущность `SHD / ШАРДОВИК` в штат ШТАБА;
- после self-report внести SHD в необходимые реестры и источники;
- детально определить обязанности и возможности SHD;
- считать `SIS / СИСАДМИН`, `KOD / КОДЕР` и `SHD / ШАРДОВИК` сотрудниками будущего контура/проекта программных разработок;
- после адаптации проинформировать остальные Сущности, особенно ARH.

На основании self-report SHD и verified GitHub evidence KOO подготовил и опубликовал новую базовую редакцию role-source:

`entity-roles-short-v2_3-approved.md`

## Граница решения

Утверждение:
- сохраняет identity существующей Сущности SHD;
- не создаёт второй SHD;
- не инициирует автоматически самостоятельный программный проект/контур;
- не создаёт unrestricted production authority;
- не передаёт SHD полномочия KOD, SIS, KOO или ARH;
- не меняет правило `capability != authority`.

Физическая загрузка новой версии во все интерфейсные Project Sources проверяется отдельно от содержательного утверждения.

---
document_type: operator-approval-record
status: approved
approval_scope: SHD_staff_role_and_SIS_KOD_SHD_future_software_contour_membership
approval_basis: explicit_operator_decision_in_current_chat
project_time: omitted; trusted project-time source not used
