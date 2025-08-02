---
id: tag:blogger.com,1999:blog-27384460.post-5495888009342530651
title: "A simple clean good looking pagination"
pubDate: 2011-02-14
author: Sumit Datta
categories: ['forums.com', 'programming']
---

We are re-writing few base codes in [forums.com](http://forums.com) and one of things re-written is the pagination logic. We needed something very simple, good looking, yet works.

The logic boiled down to having 9 slots in total for the pagination labels. First and last ones were fixed at page number 1 and n. They were labelled "First" and "Last" too. Then we chose to keep 5 slots around the current page. So if page 8 was selected, then the labels (and corresponding pages) were 4, 5, 6, 7, 8. This allows users to browse nearby pages. The rest two slots we simply divide equally on both ends. We fill the gaps between the segments with '...' which links to nothing (FALSE here).

If the current page was near the start or end then we simply print 5 slots in that end and put the rest remaining 2 slots at the other end.

If the total number of pages is 9 or less then of course no use of all this logic, simply print them serially.

Well that's it!

Here is the code, we build an array of the pagination slots.  

```

  if($num_of_pages > 9) {
    $pagination_slots = $num_of_pages > 9 ? 9 : $num_of_pages;
    $selected_slots = array();
    if($page > 3 && $page < ($num_of_pages - 3))
      $selected_slots = array_merge(array(2, '...'), range($page - 2, $page + 2), array('...', $num_of_pages - 1));
    elseif($page < 4)
      $selected_slots = array_merge(range(2, 6), array('...', $num_of_pages - 2, $num_of_pages - 1));
    elseif($page > $num_of_pages - 3)
      $selected_slots = array_merge(array(2, 3, '...'), range($num_of_pages - 5, $num_of_pages - 1));
    $pagination = array();
    $pagination[] = array('url' => '?page=1', 'title' => _('First'));
    if(count($selected_slots) > 7) {
      foreach($selected_slots as $s) {
        if($s == '...')
          $pagination[] = array('url' => FALSE, 'title' => $s);
        else
          $pagination[] = array('url' => '?page=' . $s, 'title' => $s);
      }
    }
    $pagination[] = array('url' => '?page=' . $num_of_pages, 'title' => _('Last'));
  } else {
    $pagination[] = array('url' => '?page=1', 'title' => _('First'));
    for($i = 2; $i < $num_of_pages; $i++) {
      $pagination[] = array('url' => '?page=' . $i, 'title' => $i);
    }
    $pagination[] = array('url' => '?page=' . $num_of_pages, 'title' => _('Last'));
  }

```