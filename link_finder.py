from HTMLParser import HTMLParser
from urlparse import urlparse
from urlparse import urljoin

class LinkFinder(HTMLParser):

    def __init__(self,base_url,page_url):
        HTMLParser.__init__(self)
        self.base_url = base_url
        self.page_url = page_url
        self.links = set()

    def handle_starttag(self,tag,attrs):
        if tag == 'a':
            for (attribute,value) in attrs:
                if attribute == 'href':
                    url = urljoin(self.base_url,value)
                    self.links.add(url)

    def page_links(self):
        return self.links
    

    def error(self,message):
        pass

'''
finder = LinkFinder('https://thenewboston.com','https://thenewboston.com')

html_string = """
<!DOCTYPE html>
<!--[if IE 8]>         <html class="ie8" lang="en"> <![endif]-->
<!--[if IE 9]>         <html class="ie9 gt-ie8" lang="en"> <![endif]-->
<!--[if gt IE 9]><!--> <html class="gt-ie8 gt-ie9 not-ie" lang="en"> <!--<![endif]-->
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="Welcome to thenewboston, the world's largest collection of free video tutorials on computer programming, web design, game development, and more.">    <title>thenewboston - Video Tutorials on Programming and More</title>
    <link rel='stylesheet' type='text/css' href='//fonts.googleapis.com/css?family=Open+Sans:300italic,400italic,600italic,700italic,400,600,700,300&subset=latin' >
<link rel='stylesheet' type='text/css' href='//maxcdn.bootstrapcdn.com/font-awesome/4.3.0/css/font-awesome.min.css' >
<link rel='stylesheet' type='text/css' href='https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css' >
<link rel='stylesheet' type='text/css' href='/css/main.min.css' >
<link rel='stylesheet' type='text/css' href='/css/widgets.min.css' >
<link rel='stylesheet' type='text/css' href='/css/pages.min.css' >
<link rel='stylesheet' type='text/css' href='/css/themes.min.css' >
    <script type='text/javascript' src='//ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js' ></script>
    <!--[if lt IE 9]>
    <script src="/js/html5shiv.js"></script><![endif]-->    
</head>
<body class="theme-default main-menu-fixed main-navbar-fixed">

<script>
    (function (i, s, o, g, r, a, m){
        i['GoogleAnalyticsObject'] = r;
        i[r] = i[r] || function (){
            (i[r].q = i[r].q || []).push(arguments)
        }, i[r].l = 1 * new Date();
        a = s.createElement(o), m = s.getElementsByTagName(o)[0];
        a.async = 1;
        a.src = g;
        m.parentNode.insertBefore(a, m)
    })(window, document, 'script', '//www.google-analytics.com/analytics.js', 'ga');

    ga('create', 'UA-56989641-1', 'auto');
    ga('send', 'pageview');

</script>
    

<script>var init = []; var tnb_base_path = 'https://thenewboston.com/';</script>
<div id="main-wrapper">
	
<div id="main-navbar" class="navbar navbar-inverse" role="navigation">

	<!-- Left menu toggle button -->
	<button type="button" id="main-menu-toggle">
		<i class="navbar-icon fa fa-bars icon"></i>
	</button>

	<div class="navbar-inner">

		<!-- Logo and top menu toggle (for smaller screens) -->
		<div class="navbar-header">
			<a href="https://thenewboston.com/index.php" class="navbar-brand">
				<div>
					<img alt="thenewboston Logo" src="/images/logo.png" />
				</div>
				thenewboston
			</a>
			<button type="button" class="navbar-toggle collapsed" data-toggle="collapse"
			        data-target="#main-navbar-collapse">
				<i class="navbar-icon fa fa-bars"></i>
			</button>
		</div>

		<div id="main-navbar-collapse" class="collapse navbar-collapse main-navbar-collapse">
			<div>

				<!-- Left buttons -->
				<ul class="nav navbar-nav">
                    					<li><a href="https://thenewboston.com/forum"><i class="dropdown-icon fa fa-comment"></i>&nbsp; Forum</a></li>
					<li class="dropdown">
                        <a href="#" class="dropdown-toggle" data-toggle="dropdown"><i class="dropdown-icon fa fa-youtube-play"></i>&nbsp;&nbsp; Video Tutorials</a>
                        <ul class="dropdown-menu">
                            <li><a href="https://thenewboston.com/videos_beauty.php">Beauty</a></li>
                            <li><a href="https://thenewboston.com/videos_business.php">Business</a></li>
                            <li><a href="https://thenewboston.com/videos.php">Computer Science</a></li>
                            <li><a href="https://thenewboston.com/videos_food.php">Cooking</a></li>
                            <li><a href="https://thenewboston.com/videos_health.php">Health &amp; Medicine</a></li>
                            <li><a href="https://thenewboston.com/videos_humanities.php">Humanities</a></li>
                            <li><a href="https://thenewboston.com/videos_math.php">Math</a></li>
                            <li><a href="https://thenewboston.com/videos_science.php">Science</a></li>
                            <li><a href="https://thenewboston.com/videos_social.php">Social Sciences</a></li>
                        </ul>
                    </li>
				</ul>

				<!-- Right buttons -->
				<div class="right clearfix">
                                        <ul class="nav navbar-nav pull-right right-navbar-nav">
                        <!-- Login Form -->
                        <li class="hidden-sm hidden-xs">
                            <form class="navbar-form pull-left" method="post" action="https://thenewboston.com/login.php" validate="true">
                                <div class="form-group">
                                    <input type="text" class="form-control require-validation" placeholder="Email" v-email="1" v-require="1" name="email" id="username_id"  />
                                    <input type="password" class="form-control require-validation" placeholder="Password" v-require="1" v-minlength="6" name="password" id="password_id" />
                                    <input type="submit" name="signin_submit" class="btn btn-primary" value="Login" /> 
                                    <input type="hidden" name="action" value="login" />
                                    <input type="hidden" name="3bdc935afd6a01350afeb50096d85e47" value="1" />                                </div>
                            </form>
                        </li>
                        
                        <!-- Login Link -->
                        <li class="visible-sm visible-xs"><a href="https://thenewboston.com/login.php"><i class="dropdown-icon fa fa-sign-in"></i>&nbsp; Login</a></li>
                    </ul>
                    				</div>

			</div>
		</div>

	</div>

</div>	
<div id="main-menu" role="navigation">
    <div id="main-menu-inner">
            
                
        <ul class="navigation">

            <!-- Beauty -->
            <li>
                <a href="https://thenewboston.com/videos_beauty.php">
                    <i class="menu-icon fa fa-heart"></i>
                    <span class="mm-text">Beauty</span>
                </a>
            </li>
            
            <!-- Business -->
            <li>
                <a href="https://thenewboston.com/videos_business.php">
                    <i class="menu-icon fa fa-line-chart"></i>
                    <span class="mm-text">Business</span>
                </a>
            </li>
            
            <!-- Computer Science -->
            <li>
                <a href="https://thenewboston.com/videos.php">
                    <i class="menu-icon fa fa-laptop"></i>
                    <span class="mm-text">Computer Science</span>
                </a>
            </li>
            
            <!-- Cooking -->
            <li>
                <a href="https://thenewboston.com/videos_food.php">
                    <i class="menu-icon fa fa-coffee"></i>
                    <span class="mm-text">Cooking</span>
                </a>
            </li>

            <!-- Health & Medicine -->
            <li>
                <a href="https://thenewboston.com/videos_health.php">
                    <i class="menu-icon fa fa-stethoscope"></i>
                    <span class="mm-text">Health &amp; Medicine</span>
                </a>
            </li>
            
            <!-- Humanities -->
            <li>
                <a href="https://thenewboston.com/videos_humanities.php">
                    <i class="menu-icon fa fa-bank"></i>
                    <span class="mm-text">Humanities</span>
                </a>
            </li>
            
            <!-- Math -->
            <li>
                <a href="https://thenewboston.com/videos_math.php">
                    <i class="menu-icon fa fa-plus"></i>
                    <span class="mm-text">Math</span>
                </a>
            </li>
            
            <!-- Science -->
            <li>
                <a href="https://thenewboston.com/videos_science.php">
                    <i class="menu-icon fa fa-leaf"></i>
                    <span class="mm-text">Science</span>
                </a>
            </li>
            
            <!-- Social Sciences -->
            <li>
                <a href="https://thenewboston.com/videos_social.php">
                    <i class="menu-icon fa fa-graduation-cap"></i>
                    <span class="mm-text">Social Sciences</span>
                </a>
            </li>
            
                        <div class="menu-content animated fadeIn">
                <a href="https://thenewboston.com/register.php" class="btn btn-primary btn-block btn-outline dark">Create an Account</a>
            </div>
            
        </ul>

    </div>
</div>

<div id="main-menu-bg"></div>

<div id="content-wrapper">

    <div class="row">
        <div class="col-xs-12">
            <h1 class="margin-top5 margin-bottom15 featured-video-heading">Featured Tutorial - Android App Development for Beginners</h1>
        </div>
    </div>

    <div class="row">

        <!-- Left -->
        <div class="col-md-12 col-lg-7">

            <!-- Featured video -->
            <div class="embed-responsive embed-responsive-16by9">
                <iframe class="embed-responsive-item youtube-player" src="//www.youtube.com/embed/QAbQgLGKd3Y?enablejsapi=1"
                        id="youtube-player38"
                        data-code="-u-j7uqU7sI"
                        data-token="3bdc935afd6a01350afeb50096d85e47" allowfullscreen>
                </iframe>
            </div>
            <p class="margin-top15 margin-bottom25">
                Learn everything you need to know to get started building Android apps with Google's Android Studio and Android SDK.
                Made for beginners, we will learn about setting up our environment, building menus, and even begin Android game development!
                <br>
                <a href="https://www.thenewboston.com/videos.php?cat=278&video=27335">Watch Now</a> &middot; <a href="https://www.thenewboston.com/forum/category.php?id=10">Visit Android Forum</a>
            </p>

            <!-- Brand New Courses -->
            <div class="panel">

                <div class="panel-heading">
                    <span class="panel-title">
                        <i class="panel-title-icon fa fa-fire"></i>
                        <b>Brand New Courses</b>
                    </span>
                </div>

                <div class="panel-body no-padding">


                    <table class="videos-top-courses">

                        <!-- Java -->
                        <tr>
                            <td class="video-icon-column">
                                <a href="https://thenewboston.com/videos.php?cat=31">
                                    <img alt="Java Programming" src="/images/videos/java_beginners.png" class="img video-thumbnail">
                                </a>
                            </td>
                            <td class="video-desc-column">
                                <h4 class="top-course-title">
                                    <a href="https://thenewboston.com/videos.php?cat=31">Java - Beginners</a>
                                </h4>
                                <p class="top-course-details">
                                    Java is an incredibly popular language that is used to create desktop software, games, applets, and Android apps.
                                    <a href="https://thenewboston.com/videos.php?cat=31">87 videos</a>
                                </p>
                            </td>
                        </tr>

                        <!-- C++ -->
                        <tr>
                            <td class="video-icon-column">
                                <a href="https://thenewboston.com/videos.php?cat=16">
                                    <img alt="C++ Programming" src="/images/videos/cpp.png" class="img video-thumbnail">
                                </a>
                            </td>
                            <td class="video-desc-column">
                                <h4 class="top-course-title">
                                    <a href="https://thenewboston.com/videos.php?cat=16">C++</a>
                                </h4>
                                <p class="top-course-details">
                                    One of the worlds most popular programming languages, C++ is used in many types of software including music players, video games, and many large scale applications.
                                    <a href="https://thenewboston.com/videos.php?cat=16">73 videos</a>
                                </p>
                            </td>
                        </tr>

                        <!-- PHP -->
                        <tr>
                            <td class="video-icon-column">
                                <a href="https://thenewboston.com/videos.php?cat=11">
                                    <img alt="PHP Programming" src="/images/videos/php.png" class="img video-thumbnail">
                                </a>
                            </td>
                            <td class="video-desc-column">
                                <h4 class="top-course-title">
                                    <a href="https://thenewboston.com/videos.php?cat=11">PHP</a>
                                </h4>
                                <p class="top-course-details">
                                    Server-side, HTML embedded scripting language used to create dynamic Web pages.
                                    <a href="https://thenewboston.com/videos.php?cat=11">200 videos</a>
                                </p>
                            </td>
                        </tr>

                        <!-- HTML5 -->
                        <tr>
                            <td class="video-icon-column">
                                <a href="https://thenewboston.com/videos.php?cat=43">
                                    <img alt="HTML5 Logo" src="/images/videos/html5.png" class="img video-thumbnail">
                                </a>
                            </td>
                            <td class="video-desc-column">
                                <h4 class="top-course-title">
                                    <a href="https://thenewboston.com/videos.php?cat=43">HTML5 Web Design</a>
                                </h4>
                                <p class="top-course-details">
                                    HTML5 is the future of web development. Learn to create awesome interactive websites with these tutorials.
                                    <a href="https://thenewboston.com/videos.php?cat=43">53 videos</a>
                                </p>
                            </td>
                        </tr>

                        <!-- JavaScript -->
                        <tr>
                            <td class="video-icon-column">
                                <a href="https://thenewboston.com/videos.php?cat=10">
                                    <img alt="JavaScript Programming" src="/images/videos/javascript.png" class="img video-thumbnail">
                                </a>
                            </td>
                            <td class="video-desc-column">
                                <h4 class="top-course-title">
                                    <a href="https://thenewboston.com/videos.php?cat=10">JavaScript</a>
                                </h4>
                                <p class="top-course-details">
                                    JavaScript is a scripting language that is used to create interactive effects, animations, games for the websites.
                                    <a href="https://thenewboston.com/videos.php?cat=10">40 videos</a>
                                </p>
                            </td>
                        </tr>

                    </table>

                </div>

            </div>

        </div>

        
        <div class="col-lg-4 visible-lg">

            <!-- Top 10 Security Courses -->
            <div class="panel video-category-panel panel-success">
                <div class="panel-heading">
                    <h2 class="panel-title">
                        <i class="panel-title-icon fa fa-desktop"></i>
                        Top 10 Security Courses
                    </h2>
                </div>
                <div class="panel-body">
                    <div class="list-group">
                        <a href="https://vimeo.com/album/3510171/video/135525511" class="list-group-item" target="_blank">1.&nbsp; Burp Suite<span class="item-details"> &middot; 20 videos</span></a>
                        <a href="/videos.php?cat=357" class="list-group-item">2.&nbsp; Linux<span class="item-details"> &middot; 23 videos</span></a>
                        <a href="/videos.php?cat=365" class="list-group-item">3.&nbsp; Metasploit for Network Security<span class="item-details"> &middot; 6 videos</span></a>
                        <a href="/videos.php?cat=44" class="list-group-item">4.&nbsp; Networking<span class="item-details"> &middot; 40 videos</span></a>
                        <a href="/videos.php?cat=366" class="list-group-item">5.&nbsp; Nmap<span class="item-details"> &middot; 5 videos</span></a>
                        <a href="/videos.php?cat=359" class="list-group-item">6.&nbsp; Python Network Packet Sniffer<span class="item-details"> &middot; 7 videos</span></a>
                        <a href="/videos.php?cat=98" class="list-group-item">7.&nbsp; Python<span class="item-details"> &middot; 48 videos</span></a>
                        <a href="/videos.php?cat=361" class="list-group-item">8.&nbsp; Reverse Shell<span class="item-details"> &middot; 15 videos</span></a>
                        <a href="/videos.php?cat=367" class="list-group-item">9.&nbsp; WiFi Wireless Security<span class="item-details"> &middot; 18 videos</span></a>
                        <a href="/videos.php?cat=360" class="list-group-item">10.&nbsp; Wireshark<span class="item-details"> &middot; 8 videos</span></a>
                    </div>
                </div>
            </div>

            <!-- Featured Pages -->
            <div class="panel forum-following-panel panel-warning">
                <div class="panel-heading">
                    <span class="panel-title"><i class="panel-title-icon fa fa-bookmark"></i>Featured Pages</span>
                    <div class="panel-heading-controls">
                        <div class="panel-heading-text">
                            <a href="/search.php?type=1&sort=pop&">view all...</a>
                        </div>
                    </div>
                </div>
                <div class="panel-body">
                    <a class="following-row" href="/page.php?pid=2306">
                        <img alt="Girls logo" src="/photos/users/35257/resized/9fd79de3589edff68db18bb6141025c3.jpg">
                        <span class="following-row-text">Girls<span class="item-details"> &middot; 78 followers</span></span>
                    </a>
                    <a class="following-row" href="/page.php?pid=297">
                        <img alt="thenewboston logo" src="/photos/users/2/resized/8aa8647e9d0606074a04bfb6ee64fa70.png">
                        <span class="following-row-text">thenewboston<span class="item-details"> &middot; 757 followers</span></span>
                    </a>
                    <a class="following-row" href="/page.php?pid=1706">
                        <img alt="future logo" src="/photos/users/291/resized/4492b84252ec36c351e31d851237354e.jpg">
                        <span class="following-row-text">Future<span class="item-details"> &middot; 77 followers</span></span>
                    </a>
                    <a class="following-row" href="/page.php?pid=2222">
                        <img alt="Movie Fans logo" src="/photos/users/4237/resized/8b438442aaf1377b628ae68f5cefa4f0.jpg">
                        <span class="following-row-text">Movie Fans<span class="item-details"> &middot; 33 followers</span></span>
                    </a>
                    <a class="following-row" href="/page.php?pid=763">
                        <img alt="Real Game Dev" src="/photos/users/4454/resized/be9304e0f54abb7abc77686b6ba6d307.png">
                        <span class="following-row-text">Real Game Dev<span class="item-details"> &middot; 62 followers</span></span>
                    </a>
                    <a class="following-row" href="/page.php?pid=881">
                        <img alt="Song Per Day" src="/photos/users/4454/resized/117c0964cb691257ec6462197fdac778.png">
                        <span class="following-row-text">Song Per Day<span class="item-details"> &middot; 34 followers</span></span>
                    </a>
                    <a class="following-row" href="/page.php?pid=2294">
                        <img alt="Scenery Around The World" src="/photos/users/25213/resized/83ca8275492b51a3300e415764a3e97d.jpg">
                        <span class="following-row-text">Scenery Around The World<span class="item-details"> &middot; 19 followers</span></span>
                    </a>
                    <a class="following-row" href="/page.php?pid=767">
                        <img alt="Pixelated Motivation" src="/photos/users/4454/resized/5e7c4957a7c1b8e31e45e3b62affff7c.png">
                        <span class="following-row-text">Pixelated Motivation<span class="item-details"> &middot; 54 followers</span></span>
                    </a>
                </div>
            </div>

            <!-- Top 10 Popular Forums -->
            <div class="panel forum-following-panel panel-info">
                <div class="panel-heading">
                    <span class="panel-title"><i class="panel-title-icon fa fa-comments"></i>Top 10 Popular Forums</span>
                    <div class="panel-heading-controls">
                        <div class="panel-heading-text">
                            <a href="/forum/search_forums.php">view all...</a>
                        </div>
                    </div>
                </div>
                <div class="panel-body">
                    <a class="following-row" href="/forum/category.php?id=44">
                        <img alt="C++" src="/images/forum/logos/b57c66566dd5286a036435b570d1740f.png">
                        <span class="following-row-text">C++</span>
                    </a>
                    <a class="following-row" href="/forum/category.php?id=23">
                        <img alt="Game Design / UDK / Unity" src="/images/forum/logos/23.png">
                        <span class="following-row-text">Game Design / UDK / Unity</span>
                    </a>
                    <a class="following-row" href="/forum/category.php?id=43">
                        <img alt="General Chat" src="/images/forum/logos/40b7d73b02803aace9d158fca9bde527.png">
                        <span class="following-row-text">General Chat</span>
                    </a>
                    <a class="following-row" href="/forum/category.php?id=27">
                        <img alt="HTML / CSS / Web Design" src="/images/forum/logos/145efe2aab7ca9959397d6344180b658.png">
                        <span class="following-row-text">HTML / CSS / Web Design</span>
                    </a>
                    <a class="following-row" href="/forum/category.php?id=10">
                        <img alt="Java / Android Development" src="/images/forum/logos/dfdfdb6ea30dd264d092183442b4ec5c.png">
                        <span class="following-row-text">Java / Android Development</span>
                    </a>
                    <a class="following-row" href="/forum/category.php?id=11">
                        <img alt="Javascript" src="/images/forum/logos/11.png">
                        <span class="following-row-text">Javascript</span>
                    </a>
                    <a class="following-row" href="/forum/category.php?id=28">
                        <img alt="Linux" src="/images/forum/logos/e1d4744681368d92c847480734c0ea2b.png">
                        <span class="following-row-text">Linux</span>
                    </a>
                    <a class="following-row" href="/forum/category.php?id=30">
                        <img alt="Networking" src="/images/forum/logos/bc250f3c219a9748e82320ca66ea228e.jpg">
                        <span class="following-row-text">Networking</span>
                    </a>
                    <a class="following-row" href="/forum/category.php?id=14">
                        <img alt="PHP" src="/images/forum/logos/14.png">
                        <span class="following-row-text">PHP</span>
                    </a>
                    <a class="following-row" href="/forum/category.php?id=15">
                        <img alt="Python" src="/images/forum/logos/413e73d9c942b5dc27fcfce548046a15.png">
                        <span class="following-row-text">Python</span>
                    </a>
                </div>
            </div>

        </div>

        

    </div>
</div>
</div>

<script type='text/javascript' src='//maxcdn.bootstrapcdn.com/bootstrap/3.3.5/js/bootstrap.min.js' ></script>
<script type='text/javascript' src='/js/pixel-admin.min.js' ></script>
<script type='text/javascript' src='/js/tnb-script.min.js' ></script>
</body>
</html>
"""

finder.feed(html_string)

print finder.page_links()
'''

