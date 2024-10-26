---
layout: home
title: 🏠 Home
nav_exclude: false
nav_order: 1
---

# {{ site.tagline }}
{: .mb-2 }
{{ site.description }}
{: .fs-6 .fw-300 }


{{ site.staffersnobio }}

<!--{: .success }
>Welcome to DSC 10! Make sure to read this website thoroughly and complete the items in the [Getting Started](https://dsc10.com/syllabus/#-getting-started) checklist. These are due **Sunday, September 29th at 11:59PM**.-->


<!--{: .warning }
This site is **under construction**. Anything you read here is not finalized. This disclaimer will be removed when the site is ready for Fall 2024.-->

<!--{: .success }
>The Final Exam is **this Saturday, June 8th from 7-10PM** in Solis 104 and Solis 107. You will be assigned a seat in one of these rooms.  
>
>If at least 75% of the class fills out both [SETs](https://academicaffairs.ucsd.edu/Modules/Evals/) and the internal [End-of-Quarter Survey](https://forms.gle/pNaf8hrhmjKcJg3D9), then the entire class will have **1% of extra credit added to their overall grade**. The deadline is Saturday, June 8th at 8AM.
-->

{: .success }
>**Tip: When working on assignments, use Ctrl+F on this page to search for a keyword and quickly find the relevant lecture. Click the "✏️ write" button to open a static version of the lecture for reference, which is much faster than loading it on DataHub. Also, make sure to use the [reference sheet](https://dsc-courses.github.io/bpd-reference/docs/documentation/intro/) to quickly look up `babypandas` methods and see examples of how they work.**



[Jump to the current week](#week-5-midterm-exam){: .btn }


{% for module in site.modules %}
{{ module }}
{% endfor %}