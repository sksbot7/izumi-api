from flask import Flask ,Response ,stream_with_context #line:1
import random #line:2
import requests #line:3
from data .video_urls import eypz #line:4
from data .image_urls import izumi #line:5
app =Flask (__name__ )#line:7
@app .route ('/')#line:9
def home ():#line:10
    return 'API is running somewhere!'#line:11
@app .route ('/eypz/video.mp4',methods =['GET'])#line:13
def anime ():#line:14
    O0OOOO00OO0000O00 =random .choice (eypz )#line:15
    app .logger .info (f"Selected video URL: {O0OOOO00OO0000O00}")#line:16
    @stream_with_context #line:18
    def O0O00OOOO000OOOOO ():#line:19
        try :#line:20
            with requests .get (O0OOOO00OO0000O00 ,stream =True )as OO0O0OOOOOO0OO00O :#line:21
                OO0O0OOOOOO0OO00O .raise_for_status ()#line:22
                OOOO000O00O0O00OO =OO0O0OOOOOO0OO00O .headers .get ('Content-Length')#line:23
                app .logger .info (f"Content-Length: {OOOO000O00O0O00OO}")#line:24
                for OO0O00000000OOO00 in OO0O0OOOOOO0OO00O .iter_content (chunk_size =8192 ):#line:26
                    if OO0O00000000OOO00 :#line:27
                        yield OO0O00000000OOO00 #line:28
        except requests .RequestException as O00O0O0000OO00OOO :#line:29
            app .logger .error (f"Error fetching video: {O00O0O0000OO00OOO}")#line:30
            yield b''#line:31
    O0OOOOO000O00OO00 =Response (O0O00OOOO000OOOOO (),content_type ='video/mp4')#line:33
    O0OOOOO000O00OO00 .headers ["Content-Disposition"]="inline; filename=video.mp4"#line:34
    O0OOOOO000O00OO00 .headers ["Accept-Ranges"]="bytes"#line:35
    return O0OOOOO000O00OO00 #line:36
@app .route ('/eypz/image.png',methods =['GET'])#line:38
def stream_image ():#line:39
    OO0000OO0O0OO000O =random .choice (izumi )#line:40
    app .logger .info (f"Selected image URL: {OO0000OO0O0OO000O}")#line:41
    @stream_with_context #line:43
    def OO000OOOO0OO0O0OO ():#line:44
        try :#line:45
            with requests .get (OO0000OO0O0OO000O ,stream =True )as OO00000OO0OO0OOO0 :#line:46
                OO00000OO0OO0OOO0 .raise_for_status ()#line:47
                OOO00000000O0OOOO =OO00000OO0OO0OOO0 .headers .get ('Content-Length')#line:48
                app .logger .info (f"Content-Length: {OOO00000000O0OOOO}")#line:49
                for O00O0OOOO000O0OO0 in OO00000OO0OO0OOO0 .iter_content (chunk_size =8192 ):#line:51
                    if O00O0OOOO000O0OO0 :#line:52
                        yield O00O0OOOO000O0OO0 #line:53
        except requests .RequestException as OOOOO00O00O0O0OOO :#line:54
            app .logger .error (f"Error fetching image: {OOOOO00O00O0O0OOO}")#line:55
            yield b''#line:56
    O0O000OOO000O0OO0 =Response (OO000OOOO0OO0O0OO (),content_type ='image/png')#line:58
    O0O000OOO000O0OO0 .headers ["Content-Disposition"]="inline; filename=image.jpg"#line:59
    O0O000OOO000O0OO0 .headers ["Accept-Ranges"]="bytes"#line:60
    return O0O000OOO000O0OO0 #line:61
if __name__ =='__main__':#line:63
    app .run (port =3000 ,debug =True )
