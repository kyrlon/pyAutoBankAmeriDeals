# pyAutoBankAmeriDeals

Inspired by features of [BankofAmerica-Web-Scraper](https://github.com/eshaffer321/BankofAmerica-Web-Scraper). The module utilizes Selenium to login to your Bank of America Cash Back BankAmeriDeals<string>&reg;</string> account, select all available deals, activate them, and scrape the selected deals. The scraped deals can be output in either JSON or HTML format. 

## Account 
The account credentials are stored in a json file `account_login.json`
```json
{
    "username": "",
    "password": ""
}
```
## Usage
Install dependencies from the `requirements.txt`. Preferred method is within a virtual environment and if using VScode, you can run the task `Build Python Env` to create pyvenv and install modules within that environment. To run the program:

```
python3 
```
## JSON Output Format

```json
{
    "1TIMESTAMP": {
        "CREATED": "2024-05-16 22:58:39",
        "MODIFIED": "2024-05-18 09:57:29"
    },
    "DEALS": {
        "1-800-Flowers.com": {
            "days_left": "43 day(s) left",
            "deal_info": "10% Cash Back",
            "description": "10% Cash Back Offer subject to merchant and program terms. For Cash Back Online Shopping Offers..etc...",
            "expiration_date": "06/30/24",
            "external_link": {
                "link": "https://l.cardlytics.com/?r=64nrD&xt=eTbOA%2FF0XEeqUQgxEOfyvIve7H2%2BmVc7S8W244id%2FG0J30LFyVhVm7fsCTg8njLM",
                "text": "Shop Now"
            },
            "image_png": {
                "binary_data":
                "01101001010101100100....00100" 
            }
        }
    }
}
```

## HTML Output Format
The deals  will be displayed in collapse detail tags with button features in the HTML output, enabling users to view or hide all deal details. The fields displayed in the JSON example are displayed in collapsible detail tags in the example below:

<!DOCTYPE html>
<html>
<body>
    <ul class='tree'>
        <details>
            <summary>TIMESTAMP</summary>
            <dl>
                <dt>CREATED</dt>
                <dd> 2024-05-16 22:58:39</dd>
                <dt>MODIFIED</dt>
                <dd> 2024-05-18 09:57:29</dd>
            </dl>
        </details>
        </details>
        <details>
            <summary>DEALS</summary>
            <details>
                <summary>1-800-Flowers.com</summary><img
                    src='data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAALMAAADDCAYAAADJNiAyAAAAAXNSR0IArs4c6QAAHNpJREFUeJztnXl8FeW98L/PzJwtJwFCFjYDBAgUoSBWWkXFBQW9H70qtqIFvfVTm75Y26tSe5Wr1/pawS6o91avBXnttYWqtWIVeisoKtggLSrIIoTFsBlCFkKWk7PNzPP+MZPkZGGRBEMmz9dP5Jx5nnnOM+d8z3N+zzIzoi5myrhpo1B0Z3RNYByNmkj3iULRXYlFkxgAfkPH0LWuro9CccrEEibKYIVnUDIrPIOSWeEZlMwKz6BkVngGJbPCMyiZFZ5ByazwDEpmhWdQMis8g5JZ4RmUzArPoGRWeAYls8IzKJkVnkHJrPAMSmaFZ1AyKzyDklnhGZTMCs+gZFZ4BiWzwjMomRWewejqCii6huqYySeH6jlwNMbnNXE0AbkZfoZmhhg/IJ3MYPdTo/vVWNEh3is5yqK/H+Rv+2qOm+/iIb353jfO4tL8Pl9a3TqKOFAdkz51RSPPU16fYO6qPazadeQL7Te1oC/zpg4nN91/2urWGdREYkrmnsDe6hi3vrKNfdWxNmmPTBnKjy/OA2DppsMU/nlnmzxDM4O8ePNYBvUKfCn1PRVqIjHVAfQ60aTNt1/e2q7IJ8ve6hjfeWUbDYkz+2qxSmaP8++r9nCwJt7hcoorozz41p5OqdPpQsnsYUqORHnt0/JOK++1T8v57Ei008rrbLr9aIZhRpDmmfsGdyVLPizH6sTIwLLhlS3l/NslQzqv0E6k28uMFSMUTEM3fF1dkzOO9/bv6/Qy/7qzSsl8OtENH4bvzO1pdxW7qpo7ffOn5TNhQEabPEMzg02PrxyRyZvfGdcmz8ZDdTywsgRAhRmKrmdcv3QuHtr7uHly0/3tjiebtjyNNes8VAdQ4RlUy9xDWPpJOev2t53CvnRYHyYNdlrsLWURlu+obJOnpLrjQ3tfBkpmD1OQFWJXlRPj/uGTw+3m8etak8yby+p57L39xy1zWN/Qaahp56DCDA9z1ci+nV7m1SOzOr3MzkLJ7GG+e94AOnPJja7BTV/N7bwCOxkls4cpyArxLxP6d1p5M77aj3wVZii6isenDWdIn46PwRdkpfHwlGGdUqfThZLZ44T9Gm/c+lWG9w2eRO72GZIZ5Pc3nU3Id2br0u3XMxvxKsLhXmoG8ASUR5L8cPkuVuyo+kL7TS3oy+NXjSA77cxeLuCJxflK5i/Gqt3V/HrdQd757Ohx8100pDeF3ei0KSVzD+ZI1OTDz+v47EiUw3UJIpFaBmZnk9cn2C1PaK2JxNSkSU+lb8hg6ohMIBOAo5UHscKdN/LRFXTP5lihaAcls8IzKJkVnkHJrPAMSmaFZ1AyKzyDklnhGdQ483GwbbvFY8NQb9eZjGqZj4OmOW+Pbdvout7V1VGcACXzcUgmk2iahhCiRSutODPpOTLLdv7ayyAbH0mEBpZlsb/kIJgayLY7HrM4xZdOz5GZYwstsZFYYCcBsCVY2EgZR8ZMfvOzl3jj2fVYpo1pm9hSYlp2UxEW0snftUfX4+lZPRpxvAQBQm96KtCQVpDq8gi7t+yn+O9/pN/YIBMvGo+tuUUJpzlwilUqdzU9pmWWQiKFjS2spj8ppBNOSIGQOhIdKWwgiWYLrAaD3/36r8iYH2GbrFy2Bp+lET2a4JMN2x2XJWhINOSxvyuKL4UeIzOAnfKfhYWFmRprYLshh4ZEWLDshTW8v2obiQYI+g3G5I/nH+8W84Pbf0JdbZ27q0RgK5HPAHqUzCCQUlJRU87ugztJygQmJrYb8ZoSbFuAafD60jUsXbQCq0EnGEhjxozpBAjy2L89Q6zWZOTwka3K7mFv5RlIz/kEpECzNTShkZ6eTsn+Ej7Z9YkjtDCxhIkQFpqtUVZSy+KnXsRIGvgMyeTLv07/Yf35n2dex0eInKx+5PbvixQghYVE61Fv5ZlKj/kEhASRFGhSQxc6F026iL9/vJ6dh4oxSWCKOJqIIU34y5/ehVgYny4IhEz+6fpL+a8nf4dfD5GMmQQCAfSgU6iFdMMTRVfTY2RGOqMPtgm6piOk4Kqp03j7vbcorysnSQzLakCXAj0ZQieElAkmXz6BTZs2UVcfBSnw+Qx8fh1bSrcD6cTaJtLRWgJSYrvDfc6wn+0O3tk4XU6wUp43D3Grr0RH6DEyS00ifTa6IQjYIcJkMKDvYPJHjuR37y2hUh4lITQwQc9q4IhxFOETfG3SGP7+cQXhqA9D2iSo4/wp4xBItLiGYRlESfB5soKDlXshaiNjCXbUfsqWwx9QlzxMRNZRXP4hB+v20CBjJKTJP8o2sKNhB3ESyCQ0t/GKU6XHyOzEGZbzWIKGjs8O8PVzv0FV9RG2lG4BzYeUkmlXXUZ62IcZi1Fw9ki2bP6UoD+ESRA93Isr/mkKQhdIklhWPVX1e3j29Xm8sH4ZtYEoe6yjzFv5HEu3rOSFj/7KkuK3eLroJX7+pwUkSbBm+3us3biG5954lriZRAiaZh8Vp07PkTkV4biTsOIEtQDjR4zjg6L1VMWOgh/65WRy+803EPCb+P0CIRqIyAgN/hpuLpyGka5h69KZYzEgLT1IvwFZSBlBiAbMeDXhIEwaMx7NbKDq0H56hwyCAzX2Rj5j1Y7/5aarb6JCVlBZXYE0JKZtogk1wNcReqbMLmEjhN/2c+WkK7GjNht3fkLEn8AO2Vx/20XMnnsbESuCllGHzIpxy50Xcf1tF6GHkiStKNLW0awMdPphmZmgw77SnaSl+7CtCH9d+yqXXnQBphUlENaRvZOs3/oBBxJ7nbHu9CSaMLCw0HQNKZXMHaEHTWc3TllLaJRGQkDzkSEzGF8wjjc+/DNf+coI8nx5pPUNcuEtX2PL1l08v+znaAiyeqeBXxK3owS0IMLUwADbNkiaEtOQlB+txJeTgdA1LNti4+aPicUT9MoIYEqTWCKGMEDHwBI2hs9oCjGEmnrpED2zZXadEbbEh0EAP5d87RICGT7e2fMODSJBVFSz/uAHfB49SPZAjd45Ycr3NfDk/13Cwqf+RMXeWtat2kikOopPqyNm7ce2kpw39nxqjkYYlTeKGdNuZsfmYoK+dBIN4IumcenES+lnDEAAgYQf00yg07gmRAXNHaFnyuyiCR1d6vhsg6xAJgP69OOjbR9RnYjQQJz3d2zgnInnocsohpD85ud/4q1lH3B4Zy2bi3Yy/6EF7N/zOWVVB6g6Usa+SA0fl+6lwRdky+cHWbtjC2kDBjNoxFh2HT5C5e46hoSGcm7u13ll1SukNaST1ScLTA0NDSnVaEZH6EFhhoNMWTwnEEjLxtB9SAkT8s9hy7s72H1wL3m5adQkYvj0NKQZwaqFQ/uK6d8njfm/+CFvvvgP9EQ6AdkbTevFhK9MQZgwKBZm8IDhVAw7n+qDB5h1xa1USJu06qMMzMnFJ4PMmPRt/vMv/8nN02ZhaAbCbF6RKqQ83vK+9hGtZm3a2V26//dyKNNjZHY+RKPxifuvQLg/8RoaF474Bu8UrWb5ziWMj47m6wNGk2MHQQSpOBCBeC/S9AANhxIEQxqm0YuEGWd02llc1eufeWnx6/wjrZRBt4xkev71RHvZiIoEg3ulk/RNQ69LJ4yFFRX8y9i7yEoLEC81+X8v/IXS0sPc/fDNhLP9REsttKiELHj9jTXMuG4qxVvLeeP1FYwcOZxrb5qMFrIRhu6s1RO2c4S2aCmyaD7RQLqLoRqP14v0GJnb0KaBEvjxM6RfPu8cfQtCCe4dPw3NbSh/9KN7ENW5QJyfPvwIU6+6DtMCy7YoK67mzu88gCEN7OQW/rL8fZ757Ry+/a37mXR5Pvf+5Ef88LYHqW/ws3bbk/zhuVf47ydW8M6657ju8h9g6BD09+Kbl/8fXljxc/5j9vMc2vwZ6SND5J89HGtPkjf+/D5VDTUUpe9m795q7v7p9UgpQbOBahA6Uu/tdG5F6kFKhMdb5EZ6dMzcEoHEYMjA4fj1EFUVR/DpPoQQoMGSl58je1AW2QOz+MVTj+EP6fgMAyth89muPVhRybL/fYaZt9/C0do4mzcdwEyECNCPhmgUO6aRFe4DJgS1THqFwny8ppTe6Zk89O9zeenlJwhauez7tJR0mUVIDCZeZ3L5xZdQsr2WzLQc/vzWM3z9wtEse+NF0NzpcwESH+B3ptaFid20ErB51YhAQ3j84/b20X0BNAQ+QuTlDiGgpZER7kVGRhiEhSmTaH6QPou6eC30hoaohZlM4jd8/GHxnxmYdRakw3lX5KH5Q3z66R4KCkaye1sZJDUMW9JQW8eRYpOdnxwgHAxQXV4FSZ1zzx9IKAd8msGRyhqO1tcidHjpjd8w+YpzqYtVsvfgTpIyzn3/cRvvFP2RZKIBTQOkjiANIUNgCySmuxakcdUInpe4kZ4bZrRBoGPQK9wHzRaEg2F8BLCljRQ2wufMGGq+xp9rG7/fhyEMDpdW0K/vSKQl0QznLxj2YVm1VFWVs/GtOgb1701u/wKeeHwRu4r3c6TiIDn9sjCTcNtN9xBOD6Kn2ZRXH6F3/zD1NXsRIQsrqHPuFWfx2eFtfHv6PRQUjOfhXxTSu38Yy7LQNBvLrsHQQkAa0vJjWiY+Q3MvlSBO2Dn0Cj3jK3sSCAS6LchMzyTkDznrn53xDqQQ2BL3xCj3Z1vYRKP1aJrAsmw0zUBqJpquEY/H0DWb6d+6DL9f8sG6j/ClWQw8K5PDpbVYSYNv3Xwt9fVHOVoTZd7P5/PMop/xzMLHuGnmP9NgRqixDxLVLewAfLPwOh791UP06ZvJ9m07+MEdD6LboNkGiXoLzDAyYSCSoMU1fGYALakjLOH0DcGtt7eH/lTL3Ih0zudL0/z4dAMsiYnlnuRqISUIqSFs2TiGRiDoJ2mZFIwcxeHPI2imj2iVScCXjsSi4Gs51DZUs2Pnfkadk40vmCQeNzEtwZ0P3srfV+0kEAwz6OwgaelBHp/9FNfeOgVDaASNPujCGYt4d/nfyAzl8YfXHmfuD59gW/Em4rEkAeHjnsLHOHv0COxEiIZ6i3Hj8/jja6+RmZ3O2HOH8d3Zs0DHHfGQnm6/vHtkp4AQEpskPk0nEolQF61HCA3LGcVDkxqabH7LTCuJ4dO5+topVBypgiR8tH4btVUxLjj/QoLBIGnhMNG4xpBhBUy/8SqO1tQRjUbRfBq+oI5p26xbvYsdm8rY9uEB7IhJUGYQtAajmz6ICl5f8jcWLvgDVj0MyB5OQ42OXzOoqzDpFcrgW9dfz8f/WMdZWdlU7bf42lcu5JxRE0lETLcxlj1iialqmV2kgCQ2pi3Jqs+FoxCLx4iHkuhSIDRJg16GCDijGw1WEjtUQ1wk+MrEfEL9Elw57btEo1FGTxhP/pgcjJCkMnGAQCDObf96F/FElJivlECvEJhw3uQCsvMsfvnEr4nHTXqF0xn7jdH8dsmr1OoH0YVGQIMLr7iAZ595jhuuv5NIJMGMb3+T//ntS3z17PM4dLiUovUf4UsLUS8i6KEIkVglQaMX0XgM2wZNCoTQPX8+jLrblIsEYiSwpEVx6Q4aGuoZO3wMaVoahu1HSwr27S4nETcZOWYQRyrrqSyvZciQfvj8OvtKSvn4w734fDqXXjaOjOwQAthd/BlIgxGjBmNZNiU7DpG0YoweNxwE1ByO8NbKjYSCfbjg0mFk5qSxb/chYvE4I8cMRkgNy7bZ/OEe9u8tIz2cwSVTvkplVQ2BgJ+GSJxgMIBAUF8fp1duiGTSRtNshCbI7JuOpoOUtrNuWmv/c3Zu0DOwQ+9hV6JunZaCBBK2hRQWpohjAz4EuvTjl36wnNZb2hamZeMzdJJJE3/ATzKZRBcaZlLH8IHQJUKTSExAw05KdwhNw7YtjIAOVhJb6Gju2S227ZSv+UBaFmg20rbRDR+WJZG20yG1bRvDp2MmTIQhmobdhLsW2pSguYv9pZQY7l1VpZSuzO0PZ3hBZhVmuAjAh7OmWEobIW0M3XBWtLm/zraWAE3i82tYVgLhl1haHCOokUwm8IWDSOlcrKvxrJakaWHaEAqmY1vOtDmaTdJKYBgGyaSFzx9CWhKhS6RwrudhS4nQbDTNGUGxhQ2ahq7pSJIIYaLpOg0NdaSlhZG2BKE7E4KApjefMd4UXHh88b+SOQUNgRQQEIEWi3KcVk2gCcOZkJACXdec6yi66LrRNCPnrJs2kBJ8vgA+n4Ztg9Cc1tEGdF8AicTwa9jSRjM0pHBacN3Q0d3XtG0boWn4dMP9oji2aoZTflo47E5rC+diNLrjrG1bCGE4T6Rw/vW2y0rm1gjZqHDKJ98YgYmWU8KpDZ2mpXawdDe9OYPWvFTP/ZK0LUegu2uam8Vzym3MlxoKiub9mtZBWzSe4y00AdjONT2EMyR3CuvxuhVK5uPiTjRotquBcYIBgROockKT7BZnwbTYT8iUBawpeZqu4EhKWus1oaRMmHTPvtHJoGROpbVsQrqtm/OvkOIkjGydbjdNWMimSYvUlrkxv0RguR7qraSz3D/cqyfpLaUX0k3XsFvs1/L6vcLja+eUzKm0adBSpZPtN3gt8h4LDZquEtosb0thWwkuWre8estXaZGOu+qvtayiVWZvo2RujWj9RG+76QvxRRbDN18fuuVrHSM0aGG2Tvu/G20K8yzeDaAUPQ4ls8IzKJkVnkHJrPAMSmaFZ1AyKzyDklnhGZTMCs+gZFZ4BiWzwjMomRWeQcms8AxKZoVnUDIrPIOSWeEZlMwKz6BkVngGJbPCMyiZFZ5ByazwDEpmhWdQMis8g5JZ4RmUzArPoGRWeAYls8IzKJkVnkHJrPAMSmaFZ1AyKzyDklnhGZTMCs+gZFZ4BiWzwjN44jYQO7duIh6PdXU1ujX5I4Z3dRU6jCdkXv/um5SVHujqanRr7rz/p11dhQ6jwgyFZ/BEy9zVXPOTxYyse4knnn27xbZxuQAN7Hv9Ryx9v9X2aDFvPfRLNgBwO4W/Gkbpjx9iRRcdgxdQLXMHaZa2mYmz/4txGcW89eM7mLehhiHXPco1ABffx0h3++a6UUyY0Zh/Aul71iiRO4iS+ZS5gpmPLmYcRWwub5nSLyONWOlGp9V9+TMqGcDAGcDAXgTrKtkAHK5rIL3vFcDtTBhew86UVl1xaiiZT5m3WfrQHcz7xW9bbb+C3hlQf6RRzgNEojjiltYSy8hmoit8/ZG3mTh7AmxQ4UVnoGLmTiePcOgYSe//kp0XLObKXy2G8iLmld7HvWMP8P7W+7j3V6MIApUb7mDRy19ylT2CkrnTcVri8DFSV/zijqZW+JqfLKZ+6x30u2Ax9Rvu4InS+7h36n1MfLmxY6j4Iqgwo9N5m5o6N6yAppa6OexwcTuDG1++gt4ZDURKgfcrqQ/1ol9XVNsDKJlPA4frGggOnMBEgBnDyOYQpa1Ch2suGEX91l+ygbepqUsjPBC4OJv0aC2Hu6je3R0l82lgw7M/YnPdKK781WLmTuzNvtdbdfBmPMq4jGI2uoKv+KCY9ImLmXtdHodXqRDjVBEHqmPSZ+gYevf02ohX8erz/62mszvInff/FCs8sKurccrURGKqZVZ4ByWzwjMomRWewRPjzMNGnU32gO4b7yk6h27fAdStGJo0u7oa3R4pBKZ+rKmeM5+aSKz7t8yWHsTq6koozgi6Z3OsULSDklnhGZTMCs+gZFZ4BiWzwjMomRWeQcms8AxKZoVnUDIrPIOSWeEZlMwKz6BkVngGJbPCMyiZFZ5ByazwDEpmhWdQMis8g5JZ4RmUzArPoGRWeAYls8IzKJkVnkHJrPAMSmaFZ1AyKzyDklnhGY5zea5NLLlxDmvbSyq4m3mPX0v2aapU5cq7mLtoOwD5hUt5YFr/Y9Zr8iOrmTW25b7P8SAPTIM1989k6S43YeoCFn3/nOaM5cuZP/spSo5xPM3l9Kd44RQWrGpMGc3MZ5/mklY3sgScfLR6nZ5ExTZuvaeOG548n+k5x9jOMfI4GVn28E5emzyS309pk3hCTnitudaynHbKl/PcIpj57GouYTnzZ/+MNRMa5Sljzf1zWNsoZvly5s++izUpclXt3U7ehY6AS/MXsOjxc5q+APOHNn4xyljzxFNQuJRFrvTPrZzY4kvTWE7lyrtYUHI38151ZK9ceRdzZz9J/1fvYVRqvbc+6Qg/9Ut8rxQtOOPCjMqNKykpmMaYXCD3WqZP3c66jWVOYvkG1u26hjmNLV/utTzwamoruYkNq65h4lgY9f3VKS3kOUycCiV7U8sZzaQJ/YH+XDLrGkre3UAlbcvJnvY0i1Ja7ewJ08hnD2Ut7spaxpole8gvOL3vjSfIGcPvl7TXKnecU5e5fDnzb5zC/JWuIJSx5v4pFC7c5KbdxZqVT1J44xQKW+Q7PlV7t0N+Xouf/EYJHdFHkHWsnbe+y9qpl7VsMcGVEyZf6MpdvpsShtM/NVTYtZuqE5bTPpUrf8a6yx5kev5J7tCTqdjGrbPWs6wi9XkR2bOKyH74c1rfmebD5920WUVkP//ZcYs+YZix9uEpbeJmJ/S4lgeepSkMGLPxZyzlbuZ9/xwoPwBsZ+m705j36mqyy5czf/ZMlgw6uZAlf2jzz33W0NGwNzUxj6qFU5i7KrUuzuPKz/eQP/SWFmU1xbsFdzMv9bVTvxS5I8hnd1NSe+U0lffaU5QU3M33Un4N3lw0nOmv9oeFJz4272NReE8RhW2269zQZlsFy54+CrePpHJKDmzfRPZjcPVkJ/Xw6vVcta8P25aMoZ8bT9+6OuOY8XTHYubca/le4Urmzp7idoxadqImz3Kf517L9KlPsaBoE7PGdrBztGoOGx5ZzaLvO3Fq4cN3kffs01ySW8a2d2HSvf1bZHfCDUfqufdzEh3X9svBjZcXrGp5nMUL58AjqxkFFHfsyDyCzqJjdADbUFHOa3t0brjLzTx6EIuG7+Q1J5GitRYP3TzGvclnDtNv/pzCl8o5PCWn3Rt/djhmzp52B5OB/MIHW/XwR5OX8jxr6OiTLrMptm0MO1IpuJurGr9cY29hZkFjTF3GgV2tQocURt1wN/m7VrKtMdZNDSvKdzujGnDMcpwRFlqOZJQvZ1lJSn0UX4zKJH8lyOAm8XMYPKTxcR0H9sCjj6WEGY9FYE+yTSjSSIevnF+8cA5rC0aTvyh11AFgOwfKgZRRhpOhTViREnZkDxre7j55g/rD1hdZO/UyZh2rYDdOnp4L0DKsgJSww42XU8txRB7OnFYjGJUbV1Kyaztzb3wqZescCktO79ClZ8j2cTV17K+A83IAKti/DxgCkEHe8EM8dPOF/OtJtoMda5m3PsmCVdcw5/Gn+V4hLH1iecqIAKwt2uQ8KF/OstQO2HHInjCN/FWLWVPeuF/jqAMw9jIm73qKN7c2vv6LLN3ljDoUF61oUX7xQrczCu5owwpo7NTlTmRSwQqWrSxrSsu/bCLZtC2HrU+6LfI9bTqE2dOeZtGrq5v+5kx1x7OVyCdHTi43DLcoXO527CrKeW1PUyIXTtZ59KVtTbdf/vD5IrIf3nbM2zGfUgcQrmHOI7Dg4RVMduNFpj3IzHdnMndhHotuABjNZBZTeGPz5EdTR23lXczde0f7kwspcfhSd7/m1v4cZr26gCU3TnE7GM4ExijKWFMymryUHsao7y9l5v0zKbzR3VDgdk7BGY67927WzZ5J4SI3zR1/LmtVTnGRc6PgpW59GvnSx989SQ7TH6njwKxDZL9zCAjz0OXwoZvab8r5vLmviDGzitwtYd5cMqbdeJnTdrep8uXMn72SSceYKVMoOht1u2GFp1AyKzxDt7+ppUKBCjMUXkPJrPAMSmaFZ1AyKzyDklnhGZTMCs+gZFZ4BgOgPpoAZFfXRaE4ZYQQ/H+5BEp8rxrJVQAAAABJRU5ErkJggg=='>
                <dl>
                    <dt>Days Remaining</dt>
                    <dd> 43 day(s) left</dd>
                    <dt>Expiration Date</dt>
                    <dd> 06/30/24</dd>
                    <dt>Deal Info</dt>
                    <dd> 10% Cash Back</dd>
                    <dt>Description</dt>
                    <dd> 10% Cash Back Offer subject to merchant and program terms. For Cash Back Online Shopping Offers: If a merchant processes your   order in separate transactions,.....</dd>
                    <dt>External Deal Link</dt>
                    <dd> <a href="https://l.cardlytics.com/?r=64nrD&xt=eTbOA%2FF0XEeqUQgxEOfyvIve7H2%2BmVc7S8W244id%2FG0J30LFyVhVm7fsCTg8njLM"
                            target="_blank">Shop Now</a></dd>
                </dl>
            </details>
        </details>
    </ul>
</body>
</html>
