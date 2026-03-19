+++
date = 2026-03-19
draft = false
title = 'Еженедельник OSM 815'
featureImage = 'https://weeklyosm.eu/wp-content/uploads/2026/03/815.jpg'
featureImageCap = '\[[^1^](#wn815_34170)\] | Интерфейс инструмента [«Podoma»](https://wiki.openstreetmap.org/wiki/Podoma) с картой Италии | Данные карты © [Участники OpenStreetMap](https://osmfoundation.org/wiki/Licence/Licence_and_Legal_FAQ).'
+++

26.02.2026-04.03.2026

## О нас

* StreetComplete [теперь](https://github.com/streetcomplete/StreetComplete/pull/6728) :EN-s: будет извещать о выходе нового выпуска weeklyOSM. Также в этом обновлении исправлены проблемы с расчётом статистики, появились уведомления об OSM-мероприятиях поблизости из [OpenStreetMap Calendar](https://osmcal.org) и возможность настраивать эти уведомления.

## Картографирование

* Джеймс Уир начал [обсуждение](https://www.openstreetmap.org/user/jwheare/diary/408308) противоречащих друг другу определений тега `wetland=tidalflat`.

## Картографические акции

* [^1^] Daniele [запустил](https://community.openstreetmap.org/t/dashboard-podoma-per-il-progetto-del-mese/141779) :IT-s:>>>[:RU-t:](https://community-openstreetmap-org.translate.goog/t/dashboard-podoma-per-il-progetto-del-mese/141779?_x_tr_sl=auto&_x_tr_tl=RU) экземпляр утилиты [Podoma](https://wiki.openstreetmap.org/wiki/Podoma) на платформе [облачных сервисов Викимедии](https://wikitech.wikimedia.org/wiki/Help:Cloud_Services_introduction) :EN-s: для отслеживания [проекта месяца](https://wiki.openstreetmap.org/wiki/IT:Italia/Progetto_del_Mese) :IT-s: — инициативы итальянского сообщества OpenStreetMap.

* Завершилась февральская [кампания](https://community.openstreetmap.org/t/progetto-del-mese-febbraio-2026-lampioni/141180/61) :IT-s: по картографированию от итальянского сообщества OpenStreetMap. Благодаря участникам, на карту было добавлено 100 тыс. уличных фонарей, включая даже тип лампочек и их угол поворота.

## Сообщество

* В своём последнем интервью об OpenStreetMap команда OpenCage [обсудила](https://blog.opencagedata.com/post/openstreetmap-interview-dwinnovation) :EN-s: с Deutsche Welle Innovation их разработку под названием SPOT, которая позволяет находить какое-либо место в городе по описанию объектов рядом с ним. Дискуссия развернулась вокруг того, как возник проект, технических деталей реализации и что по итогу смогли вынести для себя журналисты после года использования SPOT.

* Межведомственное управление Франции по цифровым технологиям [опубликовало](https://www.numerique.gouv.fr/sinformer/blog/la-fabrique-du-libre-panoramax-de-lutopie-a-linfrastructure-publique/) :FR-s: беседу с Кристианом Квестом о проекте Panoramax. В ней затрагиваются темы старта и разработки на ранних этапах, обсуждаются различные трудности по созданию активного пользовательского сообщества и его судьбе спустя годы.

* Группа энтузиастов MapRVA [запустила](https://en.osm.town/@yesterdays_bot) бота The Yesterdays в Мастодоне. Каждые два часа он выкладывает архивные исторические фотографии города Ричмонд (столицы штата Вирджиния) вместе с геопозицией на современных картах OSM.

## Фонд OpenStreetMap

* Совет фонда OpenStreetMap официально [представил](https://en.osm.town/@openstreetmap/116165330892920654) :EN-s: свои замечания по предложению Консорциума по открытым геоданным (Open Geospatial Consortium) о стандартизации глобальной системы географических координат (GERS) разработки Overture Maps. Фонд OSM не возражает против концепции глобальной системы географических идентификаторов, однако указывает, что географическая реальность не может быть сведена к одному авторитетному источнику. По мнению совета OSM, знания об окружающем мире создаются не только в центрах обработки данных корпораций, но и благодаря усилиям многих добровольцев по всему миру, которые картографируют улицы, районы и окружающую их среду. Поэтому фонд OSM считает, что любой стандарт, которому необходимо одобрение консорциума, должен быть достаточно гибким, чтобы учитывать как централизованные, так и децентрализованные, то есть управляемые сообществом источники геоданных.

## Карты

* Проект OpenStreetMap Americana [улучшает](https://community.openstreetmap.org/t/osm-americana-your-local-language-companion/141757) :EN-s: поддержку диалектов и многоязычности. Веб-разработчики могут установить утилиту [Diplomat](https://github.com/osm-americana/diplomat/) для экспорта языковых меток из OSM Americana на карты MapLibre.

## Программы

* GanderPL [разработал](https://www.openstreetmap.org/user/GanderPL/diary/408286) :EN-s: MCP-сервер для тегирования OSM объектов, основой для которого стал проект [iD Tagging Schema](https://github.com/openstreetmap/id-tagging-schema) редактора iD.

* Conveyal [разработал](https://medium.com/conveyal-blog/introducing-osmix-365c4b4332ef) :EN-s: Osmix — [набор библиотек](https://github.com/conveyal/osmix) для просмотра данных, поиска по ним, а также работы с форматом OpenStreetMap PBF прямо в браузере (все вычисления производятся локально, вне сторонних серверов).

* Sarath Sabarish [демонстрирует](https://www.openstreetmap.org/user/sarath%20sabarish/diary/408305) :EN-s: работу собственной утилиты SafeStreets на примере таиландского города Чиангмай: отсутствие пешеходных переходов (`highway=crossing`) приводит к низкой оценке даже в случае хорошо картографированных улиц. Для геокодирования используются Nominatim, для получения данных - Overpass API.

## Программирование

* pascal_n [рассказал](https://neis-one.org/2026/03/flappy-birds-coding-assistants) :EN-s:, как ИИ-агенты справляются с задачами кодирования, будучи встроенными прямо в среду разработки, на примере создания аналога мобильной игры Flappy Birds и веб-страницы с картой OSM, слоями GeoJSON и WMS и так далее. В статье сравниваются Microsoft Copilot, OpenAI Codex и Anthropic Claude, а результаты подтолкнули автора к тому, чтобы попробовать такой вайб-кодинг со своими студентами.

* HeiGIT [поделились рассуждениями](https://heigit.org/how-street-level-imagery-and-deep-learning-are-helping-map-global-infrastructure) :EN-s:, как использование съёмки местности вместе с методами глубокого обучения помогает находить и картографировать критически важную инфраструктуру, данных о которой нет в существующих базах. Применяя описанные методы, можно эффективней классифицировать дорожное покрытие, детектировать мусор, замерять габариты тротуаров или строить маршруты с учётом актуальных погодных условий.

## OSM в прессе

* Петя Кангалова, старший менеджер по технологическому сотрудничеству в HOT, [рассказала](https://lwn.net/Articles/1057691/) :EN-s:, как общественная организация сумела создать сложный технический продукт вокруг OpenStreetMap, призванный упростить картографирование территорий именно местными жителями, облегчить глобальные гуманитарные работы, устранение последствий стихийных бедствий и техногенных катастроф.

## Разное о картах

* НАСА и компания [DevGlobal](https://dev.global/) проведут онлайн-мероприятие, посвящённое [совместной работе](https://nasalifelines.org/data-studios/) :EN-s: по устранению таких чрезвычайных происшествий, как пожары, наводнения и оползни. Встреча длительностью в один час пройдёт 11.03.2026 в 15:00 по UTC. [Регистрация](https://nasalifelines.org/community-connect-sign-up/) бесплатна.

* Chromy [рассказал](https://news.ycombinator.com/item?id=47205637) :EN-s: про сайт [Flexport Atlas](https://atlas.flexport.com/). Это карта, частично использующая данные OpenStreetMap и на которой показываются грузовые суда (включая информацию о швартовке, стоянке или рейсе), а также порты и самолёты. Информация об объектах обновляется каждые 2 часа.

## Предстоящие события

* |Страна                                                                 |Где           |Адрес                                             |Что                                                                                                            |Когда     |
|-----------------------------------------------------------------------|--------------|--------------------------------------------------|---------------------------------------------------------------------------------------------------------------|----------|
|![flag](https://blog.openstreetmap.de/wp-uploads/2016/05/be.svg)       |              |Hogeschool Odissee Hospitaalstraat 23 Sint-Niklaas|Vereniging Leraars Aardrijkskunde (VLA) conference 2026 [:osmcalpic:](https://osmcal.org/event/4522/)          |2026-03-07|
|![flag](https://blog.openstreetmap.de/wp-uploads/2017/06/au.svg)       |Perth         |Espresso Perk U Later                             |Social Mapping Sunday: Moort-ak Waadiny / Wellington Square Perth [:osmcalpic:](https://osmcal.org/event/4539/)|2026-03-07|
|![flag](https://blog.openstreetmap.de/wp-uploads/2017/06/au.svg)       |Perth         |Espresso Perk U Later                             |Social Mapping Sunday: Moort-ak Waadiny / Wellington Square Perth [:osmcalpic:](https://osmcal.org/event/4540/)|2026-03-08|
|![flag](https://blog.openstreetmap.de/wp-uploads/2016/07/dk.svg)       |København     |Cafe Bevar's                                      |~~OSMmapperCPH~~ [:osmcalpic:](https://osmcal.org/event/4479/)                                                 |2026-03-08|
|![flag](https://blog.openstreetmap.de/wp-uploads/2016/01/in.svg)       |Delhi         |Books and Beans Café, Mayur Vihar Phase 1         |OSM Delhi Mapping Party No.27 (East Zone) [:osmcalpic:](https://osmcal.org/event/4348/)                        |2026-03-08|
|![flag](https://blog.openstreetmap.de/wp-uploads/2016/01/ca.svg)       |London        |Social Sciences Centre - Western University       |Friends of MSF UWO Mapathon [:osmcalpic:](https://osmcal.org/event/4517/)                                      |2026-03-09|
|![flag](https://weeklyosm.eu/wp-content/uploads/sites/4/2021/09/cz.svg)|Brno          |Geografický ústav, PřF MUNI, Brno                 |Březnový brněnský Missing Maps Mapathon na Geografickém ústavu [:osmcalpic:](https://osmcal.org/event/4512/)   |2026-03-09|
|                                                                       |              |                                                  |Missing Maps : Mapathon en ligne - CartONG [fr] [:osmcalpic:](https://osmcal.org/event/4293/)                  |2026-03-09|
|![flag](https://blog.openstreetmap.de/wp-uploads/2016/02/fr.svg)       |Grenoble      |La Turbine Coop                                   |Découverte d'OpenStreetMap [:osmcalpic:](https://osmcal.org/event/4563/)                                       |2026-03-09|
|![flag](https://blog.openstreetmap.de/wp-uploads/2016/05/tw.svg)       |臺北市           |MozSpace Taipei                                   |OpenStreetMap x Wikidata Taipei #86 [:osmcalpic:](https://osmcal.org/event/4322/)                              |2026-03-09|
|![flag](https://blog.openstreetmap.de/wp-uploads/2016/05/es.svg)       |Zaragoza      |Online                                            |Mappy Hour OSM España [:osmcalpic:](https://osmcal.org/event/4602/)                                            |2026-03-10|
|![flag](https://blog.openstreetmap.de/wp-uploads/2016/01/de.svg)       |Hamburg       |Voraussichtlich: "Variable", Karolinenstraße 23   |Hamburger Mappertreffen [:osmcalpic:](https://osmcal.org/event/4399/)                                          |2026-03-10|
|![flag](https://www.weeklyosm.eu/wp-content/uploads/2018/11/ie.svg)    |Cork          |Logitech, Cork, Ireland                           |~~Logitech Missing Maps - Office Mapathon~~ [:osmcalpic:](https://osmcal.org/event/4510/)                      |2026-03-11|
|![flag](https://blog.openstreetmap.de/wp-uploads/2016/01/us.svg)       |Reston        |George Mason University, HUB VIP 3                |The GAIN Mapathon [:osmcalpic:](https://osmcal.org/event/4531/)                                                |2026-03-11|
|![flag](https://blog.openstreetmap.de/wp-uploads/2016/02/ch.svg)       |Zürich        |Bitwäscherei Zürich                               |185. OSM-Stammtisch Zürich [:osmcalpic:](https://osmcal.org/event/4450/)                                       |2026-03-11|
|![flag](https://blog.openstreetmap.de/wp-uploads/2016/02/ch.svg)       |Zürich        |Schweizerisches Rotes Kreuz                       |Missing Maps Zürich Mapathon [:osmcalpic:](https://osmcal.org/event/4558/)                                     |2026-03-11|
|![flag](https://blog.openstreetmap.de/wp-uploads/2016/02/it.svg)       |Milano        |Building 3A Ground Floor - Politecnico di Milano  |PoliMappers Maptedì [:osmcalpic:](https://osmcal.org/event/4599/)                                              |2026-03-12|
|![flag](https://blog.openstreetmap.de/wp-uploads/2016/01/de.svg)       |Berlin        |Dieselhaus, Forum a. d. Museumsinsel 10           |213. OSM-Stammtisch Berlin-Brandenburg [:osmcalpic:](https://osmcal.org/event/4600/)                           |2026-03-12|
|![flag](https://blog.openstreetmap.de/wp-uploads/2016/01/de.svg)       |München       |WikiMUC                                           |Münchner OSM-Treffen [:osmcalpic:](https://osmcal.org/event/4343/)                                             |2026-03-12|
|![flag](https://blog.openstreetmap.de/wp-uploads/2016/01/de.svg)       |              |Magrathea Laboratories Chaos Computer Club Fulda  |OSM-Tools: Wenn die Welt zur Spielwiese wird [:osmcalpic:](https://osmcal.org/event/4598/)                     |2026-03-13|
|![flag](https://blog.openstreetmap.de/wp-uploads/2016/05/be.svg)       |Leuven        |Romaanse Poort                                    |Camera's in kaart brengen [:osmcalpic:](https://osmcal.org/event/4549/)                                        |2026-03-14|
|                                                                       |              |                                                  |Missing Maps London: (Online) Mid-Month Mapathon [eng] [:osmcalpic:](https://osmcal.org/event/4243/)           |2026-03-17|
|![flag](https://blog.openstreetmap.de/wp-uploads/2016/02/fr.svg)       |Lyon          |Tubà                                              |Réunion du groupe local de Lyon [:osmcalpic:](https://osmcal.org/event/4305/)                                  |2026-03-17|
|![flag](https://blog.openstreetmap.de/wp-uploads/2016/01/de.svg)       |Bonn          |Dotty's                                           |198. OSM-Stammtisch Bonn [:osmcalpic:](https://osmcal.org/event/4354/)                                         |2026-03-17|
|![flag](https://blog.openstreetmap.de/wp-uploads/2016/01/de.svg)       |              |Online                                            |Lüneburger Mappertreffen (online) [:osmcalpic:](https://osmcal.org/event/4369/)                                |2026-03-17|
|![flag](https://blog.openstreetmap.de/wp-uploads/2016/02/fr.svg)       |              |MJC de Vienne                                     |Réunion des contributeurs de Vienne (38) [:osmcalpic:](https://osmcal.org/event/4562/)                         |2026-03-18|
|![flag](https://blog.openstreetmap.de/wp-uploads/2016/02/at.svg)       |Stainach-Pürgg|Online                                            |20. Österreichischer OSM-Stammtisch (online) [:osmcalpic:](https://osmcal.org/event/4438/)                     |2026-03-18|
|                                                                       |              |                                                  |Online Mapathon - Ärzte ohne Grenzen [:osmcalpic:](https://osmcal.org/event/4513/)                             |2026-03-18|
|![flag](https://blog.openstreetmap.de/wp-uploads/2016/01/de.svg)       |Heidelberg    |DEZERNAT#16                                       |Rhein-Neckar OSM Treffen // Intro iD-Editor [:osmcalpic:](https://osmcal.org/event/4509/)                      |2026-03-19|
|                                                                       |              |                                                  |OSMF Engineering Working Group meeting [:osmcalpic:](https://osmcal.org/event/4601/)                           |2026-03-20|
|![flag](https://weeklyosm.eu/wp-content/uploads/sites/4/2021/09/cz.svg)|Olomouc       |Přírodovědecká fakulta Univerzity Palackého       |Missing Maps Day Olomouc 2026 [:osmcalpic:](https://osmcal.org/event/4545/)                                    |2026-03-21|
|![flag](https://blog.openstreetmap.de/wp-uploads/2016/01/de.svg)       |              |                                                  |Frühlingsmapping 2026 [:osmcalpic:](https://osmcal.org/event/4542/)                                            |2026-03-22|
|                                                                       |              |                                                  |Missing Maps : Mapathon en ligne - CartONG [fr] [:osmcalpic:](https://osmcal.org/event/4294/)                  |2026-03-23|