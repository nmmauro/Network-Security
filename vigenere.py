def VCbreaker(ctext, pad):

    ctext = list(ctext)
    pad = list(pad)
    message = ""
    count = 0
    for i in ctext:
        if i not in ['.',',','!',' ']:
            original = ord(i) - 65
            key = ord(pad[count % len(pad)]) - 65
            new = chr(((original - key) % 26) + 65)
            message += new
            count += 1
        else:
            message += i
    return message

print(VCbreaker("UMLKLNGLEDFXY", "CIJTHUUHMLFRU"))

print(VCbreaker("TWT CMGWI ZJ TWT AIOEAP XO QT DICJGP MN IWPMR ETCWOCH, SSUHTD, TAETCW, ACS PJFTREW, AVPTRSI JYVEPHZRAQAP WEPGNLEH PYH STXKYRTH, DLAAA YST QT GMOAPEID, PCO RO LPCVACID WHPAW MSHJP, FUI JASN EGZFAQAP GAJHP, WUEEZVTTS MC OPIS SR PUQMRBPEMOC, PYH PPGEMCJALVLN SPWCGXMMNV ISI PAPNI TD QP WEPGNLES, PYH TWT AIRHDYW OG ISMNVH ES BT HPMZTS.", "APPLE"))

# Deciphered Message: THE RIGHT OF THE PEOPLE TO BE SECURE IN THEIR PERSONS, HOUSES, PAPERS, AND EFFECTS, AGAINST UNREASONABLE SEARCHES AND SEIZURES, SHALL NOT BE VIOLATED, AND NO WARRANTS SHALL ISSUE, BUT UPON PROBABLE CAUSE, SUPPORTED BY OATH OR AFFIRMATION, AND PARTICULARLY DESCRIBING THE PLACE TO BE SEARCHED, AND THE PERSONS OR THINGS TO BE SEIZED.
