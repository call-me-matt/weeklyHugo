# TO TACKLE:

The following aspects need to be investigated and solutions to be developed

* featureImageCap with superscript and links
* do we want to show also unavailable translations?
* rss feeds for all languages with unchanged adress (de/feed and feed?lang=de)
* upcoming event flags have a caption
* theme polishing, use hugo mod instead of theme git submodule
* translation flag icons :FR-s: »> :DE-t:
* use pagefind for search (multi lang support and faster, see github action deploy script)
* workflow of publishing, editing (started with migration/publish_osmbc_md.py)
* migration of previous blog entries (export database to content folder as markups)
* comment function with moderation
* migration of previous comments 
* email subscription function

# TODO:

The following aspects have been identified and need to be completed in order to migrate weeklyOSM from wordpress to hugo

## OSMBC markdown exporter

* lead pictures must be without size attribute  =1413x959 --> see migration/transform_osmbc_leadimage.py
* lead picture must be moved to archetypes (featureImage, featureImageCap, featureImageAlt) --> see migration/transform_osmbc_leadimage.py
* referene to articles with shortcodes (li id to be replaced by {{ < anchor "id-slug" > }})
* footnotes also need a shortcode (^1^ to be translated into {{< sup "1" >}})
* upcoming events category shall not be a list item
* include also non-translated languages in markdown export --> see migration/create_shadow_files.py

## OSMBC admin config

* footer with author information to be included/converted to markdown: https://osmbc.openstreetmap.de/config/editorstrings

## Manual migration steps

* migration of previous images (copy wp-content folder to static/wp-content)
