def get_headers():
    headers = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
        "Connection": "keep-alive",
        "Content-Type": "text/plain",
        "Cookie": (
            "SCOUTER=x65no98bl0q0qu; TKLINK_SES=AAAAl6M9fJhhSOMI665PoGffdue7VGBF7b1H_"
            "GivFUv8AqIzGBWJpmmSqp3H6LXvnICpdYa1U2wzKu-io0KB1kaGJfBpejS770N1OtElPBFX3"
            "EItQhFP-fqAW52HIqzKceK6trpcHDsKxHOQmXc8HTN_4dZpaem-ta2ToLhYIFsWq2Hg-yG7o"
            "aOq7r5vqROHqo2HAGTi6PmzmJbEwohEOfAg2D4.A; TKLINK_CHK=AAAA2A2iLld99EJ-AOR"
            "xN4feoTSrhVZxtIwC0xfVRXmGR_P09o5d2lFg7UDtZ-84fZ7EQ87pjFupEYpV7jRpOUG07dE"
            "Loj5iqFs8zwyGSPZyN6fSlHBzyMO1KdLq7R7J6Gn957r7CP6_nYp1kDPE4wQnuuSr9xtiIcP"
            "uWNAkrslJX05507FzX2XWL-JYsWuwsmRrxYIvjwcuraO4Oh5TAjoWfG3KV8dY_ybEOlaX81U"
            "2gG3qL6FWzPR2JMtrfULhJT3NQxR6xwrC3fVhK6Cd_MDhzwewHkZZWKtSZ1JbMDu-IWGM.n4"
            "qcUp3_wubW62bB9719fSBs1nCDCmKHK1TNMMKt76lHliVAOEsEa7-SA3y6TMVQupb1DrMsho"
            "mJzGy1019ajpoipsdyRgrreEQBHInJbkVbOFWBetHr_URoJ35N92Lkxm3i-k6pp3D3W2R-hW"
            "Oni9m1UxccS_K7k_QVRcwVaVzHPMIE01pzr0xS_P14P8jqBeCbiaID-Jx9i05XabnEd8sr-K"
            "1fCEA5UWvNqAO4RWhnnmLXT2SC5yiAciHOdNulZTwj1ft7c9GEGXyti_unm93AZBCgxuh2Fg"
            "WgB83xIzCtcFACVwu0KRylklE7uK2j33F57ZXexy3VjpDGRviCnw; TKLINK=WXZHHT062DB"
            "xQuxKdELDGNJZ67%2B%2FvlSYBk6x6H8hdbLuRpUAwzNGaAWgeUvICx4jdXg%2Bi6mZJGxna"
            "SkyeBiTkeoeVcvgpu%2FgzwCmuy4OBtAh%2FzMQaK%2FWsLrk1GnaB0%2Fy8Xsnfz8ENQoQb"
            "btCPrMPydZJKfPO3dOpPFZLaSW6j9cgSu2%2FB%2FZAc2urDlbqjpNC0jS57Bbc%2B71fRHg"
            "I%2BLGN9KTQgn%2BtNJxm9mwLf8HDZPVXBb4CnfmVOl2nT23yscmLyLmG3hpvSGJOBrhNhHZ"
            "9yV9SrVKOmYOT09EbEcyo5AFdjH8r3mmqG%2BAoLIqDcNQPqwV0B49MRfvwmucj3M08k%2B3"
            "0hGIdBenMIMTaqeGSTLLd8hQvUZ6Fl1Z4Zv2%2BikXD; VIEW_TKLINK_ID=jas******@na"
            "ver.com; TKLINK_PAYCO_VIP_FLAG=false; DRTOUR=ELJfBPwcypV4eGUKUwUPhcaD0Cv"
            "5UCliYEzvKIL7ZJcMddr0Q%2BAkyP6uVqpn6DPRs0IKYeq%2FgNnh6g%2F%2BvyLXwvHUX1D"
            "GNiWqeVlhE85qRmQ%3D; ACEFCID=UID-667A690EA9F60D4624D36DAF; ALBS2A3987686"
            "3068=1719298318583786660; AUFBS2A39876863068=1719276729395701533|2|17192"
            "76729395701533|1|1719276729366601533; ACEUACS=1719276729366601533; _ga=G"
            "A1.1.1868513341.1719298321; JSESSIONID=ACC2E0ACCCE90790ADDA4A85BA6BADC4."
            "WAS1; SCOUTER=x5bviabvj1movj; mxuid=d0b812dc-2d9d-4aef-9567-c69dae85eb98"
            "; AUBS2A39876863068=1719298318583786660%7C2%7C1719276729395701533%7C1%7C"
            "1719276729366601533%7C1; cro_uv_ymd=20240625; _fbp=fb.2.1719298416181.67"
            "8737264141287245; JSESSIONID=421D79226D95E6753D13144207610391.WAS1; TKLI"
            "NK_CAPTCHA_KEY=fc7e0188-e151-466f-8640-373bddb1dd23; TKLINK_CHK_NO=VkvSc"
            "eEjNSfWKMMlloY0tg==; ARBS2A39876863068=httpswwwticketlinkcokrreserveplan"
            "schedule1259310931menuIndexreservehttpswwwticketlinkcokrreserveproduct49"
            "070scheduleId1259310931; TKLINK_CHK_KEY=wihenuOMzrVdJoblvoC+APZcmF3Yu8Uz"
            "v2KFeUrvydIZtJLhFGqMqHTRKsrol/yquuUs+zcTKn9T8rnl9V1QnQ==; gateKey_ID=500"
            "3%3A201%3Akey%3D732C879049126D4F6C720E931CD17D11B11665ECB80980B99BE0A8F4"
            "DA054F0711E847C52A0576A671B969BC7E9F7568E3A5AA3C7C83CEE1DC4D100E8740DE94"
            "3A0E36056CAA6BEFEBABC9ADAA6D136204858114157839352A2A45F86423525701FC3507"
            "33CD03600781D130B6DBECFE2C342C312C302C30%26nwait%3D0%26nnext%3D0%26tps%3"
            "D0.000000%26ttl%3D5%26ip%3Dwait.ticketlink.co.kr%26port%3D80; _ga_PVZX56"
            "STJJ=GS1.1.1719298320.1.1.1719298499.60.0.0; ASBS2A39876863068=171929831"
            "8583786660%7C1719298515274735631%7C1719298318583786660%7C0%7Chttpsidpayc"
            "ocom"
        ),
        "Host": "www.ticketlink.co.kr",
        "Referer": "https://www.ticketlink.co.kr/reserve/plan/schedule/1259310931?menuIndex=reserve",
        "Sec-Ch-Ua": '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": '"Windows"',
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
    }
    return headers