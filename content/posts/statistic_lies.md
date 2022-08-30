---
title: "How to lie using statistics"
date: 2022-08-29T15:01:17+02:00
show_reading_time: true
draft: false
featured_image: '/images/post_banners/statistics.jpeg'
katex: true

custom_table: true

tags: ["machine learning", "Python"]
summary: "It always bothers me when people sell some perentages they calculated some how as 'statistics', particularly in the media.

Thus, I would like this post to be a quick introduction, based on examples, on how manipluative some badly done statistics can be.
"
---

## 1. The Simpsons Paradox


This one is my absolute favourite!
If you see this the first time and it does not drop your jaw, then you are either much smarter than me or you may have to read it again :)

Let's consider the contentious topic of gender equality.
In my example, we shall consider a University. The administration want to make sure their addmissions are fair, so the gather some number and are shocked:

<table>
  <tr>
    <td rowspan = "2"><b></b></td>
    <td colspan="3"><b>male</b></td>
    <td colspan="3"><b>female</b></td>
  </tr>
  <tr>
    <td><b>applied</b></td>
    <td><b>accepted</b></td>
    <td><b>%</b></td>
    <td><b>applied</b></td>
    <td><b>accepted</b></td>
    <td><b>%</b></td>
  </tr>
    <tr>
    <td><b>All Departments</td>
    <td>2701</td>
    <td>1204</td>
    <td style="background-color:#B4EFA3">44.6</td>
    <td>1835</td>
    <td>573</td>
    <td style="background-color:#E47B7B">31.2</td>
  </tr>
</table>

<div class="boxWarning">It seems like women are disavantaged overall!</div>

It appears that womean are significantly disavantaged in college addmissions!!
The administration wants to figure out who is to blame. The uni has 6 different departments (A-F), so they dig down into these, to see whos to blame.

The results are unexpected.

<table>
  <tr>
    <td rowspan = "2"><b>Department</b></td>
    <td colspan="3"><b>male</b></td>
    <td colspan="3"><b>female</b></td>
  </tr>
  <tr>
    <td><b>applied</b></td>
    <td><b>accepted</b></td>
    <td><b>%</b></td>
    <td><b>applied</b></td>
    <td><b>accepted</b></td>
    <td><b>%</b></td>
  </tr>
    <tr>
    <td><b>A</td>
    <td>825</td>
    <td>528</td>
    <td style="background-color:#E47B7B">64.0</td>
    <td>108</td>
    <td>89</td>
    <td style="background-color:#B4EFA3">82.4</td>
  </tr>
  </tr>
    <tr>
    <td><b>B</td>
    <td>560</td>
    <td>353</td>
    <td style="background-color:#E47B7B">63.0</td>
    <td>25</td>
    <td>17</td>
    <td style="background-color:#B4EFA3">68.0</td>
  </tr>

  </tr>
    <tr>
    <td><b>C</td>
    <td>325</td>
    <td>110</td>
    <td style="background-color:#E1E47B">33.8</td>
    <td>593</td>
    <td>202</td>
    <td style="background-color:#E1E47B">34.1</td>
  </tr>

  </tr>
    <tr>
    <td><b>D</td>
    <td>417</td>
    <td>138</td>
    <td style="background-color:#E47B7B">33.1</td>
    <td>375</td>
    <td>131</td>
    <td style="background-color:#B4EFA3">34.9</td>
  </tr>

  </tr>
    <tr>
    <td><b>E</td>
    <td>201</td>
    <td>53</td>
    <td style="background-color:#E47B7B">26.4</td>
    <td>393</td>
    <td>110</td>
    <td style="background-color:#B4EFA3">28.0</td>
  </tr>

  </tr>
    <tr>
    <td><b>F</td>
    <td>373</td>
    <td>22</td>
    <td style="background-color:#E47B7B">5.9</td>
    <td>341</td>
    <td>24</td>
    <td style="background-color:#B4EFA3">7.0</td>
  </tr>
</table>

<div class="boxWarning">It seems like men are disavantaged in every single department!</div>


The above is the crux of the Simpsons paradox. Even using the exact same raw-data. By simply grouping the data differently, one can obtain seemingly opposite insights. You can think of it as the gerrymandering of statistics ;)

In fact, I did not fully make up the above data, but took inspiration from the [Berkeley admission data](https://en.wikipedia.org/wiki/Simpson's_paradox#Examples).

<!-- <div class="boxBell">Disclaimer</div>
<div class="boxCheck">Check</div>
<div class="boxComment">Comment</div>
<div class="boxHeart">Heart</div>
<div class="boxInfo">Info</div>
<div class="boxPlus">Plus</div>
<div class="boxStar">Star</div>
<div class="boxWarning">Warning </div> -->


