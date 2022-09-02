---
title: "EU Covid certificate decoder"
date: 2022-08-19T15:01:17+02:00
show_reading_time: true
draft: false
featured_image: '/images/post_banners/qr_banner.png'
math: true
tags: ["Python"]
summary: " A small little webtool that allows you to read out the information stored in your EU Covid certificate (Green Pass).
"
---
[Github](https://github.com/scheuclu/qr_code_reader)&nbsp;&nbsp;
[Deployed](https://scheuclu-qr-code-reader-webpage-kth84d.streamlitapp.com/)


## Background
I've always been intrigued as to how the digital COVID certificate works. Especially after I realized that the [CovPassCheck]([TODO](https://play.google.com/store/apps/details?id=de.rki.covpass.checkapp&hl=en_GB&gl=US)) app works completely offline. So, no database is being queried to check the validity of a QR code or the date of last vaccination. Instead, all the data must be contained within the QR code.

## Findings

- The codes ares standard model 1 QR codes of type 6
- The data in the QR-code is base45 encoded
- The data has been compressed with zlib before encoding
- The data is digitally signed with a private key, e.g. from Robert Koch Institute.
  - The public key can be used on the extracted data to verify this signature.

We can very easily undo all of these steps, with simple Python modules.


## Application

I built a very lighweight web-app that allows you to decode your QR-code.
The whole application with logic is just 60 lines of Pyhton.(Check out [streamlit](https://streamlit.io)❤️ )

Here's how it works:
{{< youtube nmRsv5Ye4IU >}}



