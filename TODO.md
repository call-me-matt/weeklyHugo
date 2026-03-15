TO TACKLE:

- featureImageCap with superscript and links
- language selector is available below blog posts but has no text?
- do we want to show also unavailable ones?
- rss feeds for all languages with unchanged adress (de/feed and feed?lang=de)
- theme polishing, use hugo mod instead of theme git submodule, favicon
- social media preview
- translation flag icons :FR-s: »> :DE-t:
- workflow of publishing, editing
- search
- comment function with moderation
- email subscription function

TODO:

- lead pictures must be without size attribute =1413x959
- lead picture must be moved to archetypes (featureImage, featureImageCap, featureImageAlt)
- footer with author information to be included/converted to markdown: <https://osmbc.openstreetmap.de/config/editorstrings>
- referene to articles with shortcodes (li id to be replaced by {{ < anchor "id-slug" > }})
- footnotes also need a shortcode (^1^ to be translated into {{< sup "1" >}})
- migration of previous blog entries and comments
- change the `page.Params.featured` variable to use `site.Params.featured = <number>` instead, so that one does not need to assign and unassign the value for each issue
