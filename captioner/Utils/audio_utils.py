<!doctype html>
<html class="">
	<head>
		<meta charset="utf-8" />
		<meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=no" />
		<meta name="description" content="We’re on a journey to advance and democratize artificial intelligence through open source and open science." />
		<meta property="fb:app_id" content="1321688464574422" />
		<meta name="twitter:card" content="summary_large_image" />
		<meta name="twitter:site" content="@huggingface" />
		<meta name="twitter:image" content="https://cdn-thumbnails.huggingface.co/social-thumbnails/spaces/seungheondoh/LP-Music-Caps-demo.png" />
		<meta property="og:title" content="utils/audio_utils.py · seungheondoh/LP-Music-Caps-demo at main" />
		<meta property="og:type" content="website" />
		<meta property="og:url" content="https://huggingface.co/spaces/seungheondoh/LP-Music-Caps-demo/blob/main/utils/audio_utils.py" />
		<meta property="og:image" content="https://cdn-thumbnails.huggingface.co/social-thumbnails/spaces/seungheondoh/LP-Music-Caps-demo.png" />

		<link rel="stylesheet" href="/front/build/kube-0f9fcea/style.css" />

		<link rel="preconnect" href="https://fonts.gstatic.com" />
		<link
			href="https://fonts.googleapis.com/css2?family=Source+Sans+Pro:ital,wght@0,200;0,300;0,400;0,600;0,700;0,900;1,200;1,300;1,400;1,600;1,700;1,900&display=swap"
			rel="stylesheet"
		/>
		<link
			href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;600;700&display=swap"
			rel="stylesheet"
		/>

		<link
			rel="preload"
			href="https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.12.0/katex.min.css"
			as="style"
			onload="this.onload=null;this.rel='stylesheet'"
		/>
		<noscript>
			<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.12.0/katex.min.css" />
		</noscript>

		<link rel="canonical" href="https://huggingface.co/spaces/seungheondoh/LP-Music-Caps-demo/blob/main/utils/audio_utils.py">  <!-- HEAD_svelte-1oal594_START --><style>.blob-line-num::before {
			content: attr(data-line-num);
		}
	</style><!-- HEAD_svelte-1oal594_END -->

		<title>utils/audio_utils.py · seungheondoh/LP-Music-Caps-demo at main</title>

		<script
			defer
			data-domain="huggingface.co"
			event-loggedIn="true"
			src="/js/script.pageview-props.js"
		></script>
		<script>
			window.plausible =
				window.plausible ||
				function () {
					(window.plausible.q = window.plausible.q || []).push(arguments);
				};
		</script>
		<script>
			window.hubConfig = {"features":{"signupDisabled":false},"sshGitUrl":"git@hf.co","moonHttpUrl":"https:\/\/huggingface.co","captchaApiKey":"bd5f2066-93dc-4bdd-a64b-a24646ca3859","captchaDisabledOnSignup":true,"datasetViewerPublicUrl":"https:\/\/datasets-server.huggingface.co","stripePublicKey":"pk_live_x2tdjFXBCvXo2FFmMybezpeM00J6gPCAAc","environment":"production","userAgent":"HuggingFace (production)","spacesIframeDomain":"hf.space","spacesApiUrl":"https:\/\/api.hf.space","docSearchKey":"ece5e02e57300e17d152c08056145326e90c4bff3dd07d7d1ae40cf1c8d39cb6","logoDev":{"apiUrl":"https:\/\/img.logo.dev\/","apiKey":"pk_UHS2HZOeRnaSOdDp7jbd5w"}};
		</script>
		<script type="text/javascript" src="https://de5282c3ca0c.edge.sdk.awswaf.com/de5282c3ca0c/526cf06acb0d/challenge.js" defer></script>
	</head>
	<body class="flex flex-col min-h-dvh bg-white dark:bg-gray-950 text-black ViewerBlobPage">
		<div class="flex min-h-dvh flex-col">
	<div class="SVELTE_HYDRATER contents" data-target="MainHeader" data-props="{&quot;authLight&quot;:{&quot;csrfToken&quot;:&quot;eyJkYXRhIjp7ImV4cGlyYXRpb24iOjE3MzA4Nzg1NDY1NDgsInVzZXJJZCI6IjY2YjIxYTA4ZGYxZTUzODMxZTAwYmVkMyJ9LCJzaWduYXR1cmUiOiIyMzE1ZDhlNmE4MjI1NzViZDM0ZDE1YjUyOGE0OTc2NmQ4NGZjNzI3YTE4YzhkMDQzNzMzMzkzMTcxMzQwMTc4In0=&quot;,&quot;hasHfLevelAccess&quot;:false,&quot;u&quot;:{&quot;avatarUrl&quot;:&quot;/avatars/c36a740672ff0acce1d7d9f6dbb97b46.svg&quot;,&quot;isPro&quot;:false,&quot;orgs&quot;:[],&quot;user&quot;:&quot;ghstmnnn&quot;,&quot;canPost&quot;:false,&quot;canHaveBilling&quot;:true,&quot;canCreateOrg&quot;:true,&quot;theme&quot;:&quot;light&quot;,&quot;notifications&quot;:{&quot;org_suggestions&quot;:false}}},&quot;classNames&quot;:&quot;&quot;,&quot;avatarUrl&quot;:&quot;/avatars/c36a740672ff0acce1d7d9f6dbb97b46.svg&quot;,&quot;isWide&quot;:false,&quot;isZh&quot;:false,&quot;user&quot;:&quot;ghstmnnn&quot;,&quot;unreadNotifications&quot;:0,&quot;csrf&quot;:&quot;eyJkYXRhIjp7ImV4cGlyYXRpb24iOjE3MzA4Nzg1NDY1NDgsInVzZXJJZCI6IjY2YjIxYTA4ZGYxZTUzODMxZTAwYmVkMyJ9LCJzaWduYXR1cmUiOiIyMzE1ZDhlNmE4MjI1NzViZDM0ZDE1YjUyOGE0OTc2NmQ4NGZjNzI3YTE4YzhkMDQzNzMzMzkzMTcxMzQwMTc4In0=&quot;,&quot;canCreateOrg&quot;:true}"><header class="border-b border-gray-100 "><div class="w-full px-4 container flex h-16 items-center"><div class="flex flex-1 items-center"><a class="mr-5 flex flex-none items-center lg:mr-6" href="/"><img alt="Hugging Face's logo" class="w-7 md:mr-2" src="/front/assets/huggingface_logo-noborder.svg">
				<span class="hidden whitespace-nowrap text-lg font-bold md:block">Hugging Face</span></a>
			<div class="relative flex-1 lg:max-w-sm mr-2 sm:mr-4 md:mr-3 xl:mr-6"><input autocomplete="off" class="w-full dark:bg-gray-950 pl-8 form-input-alt h-9 pr-3 focus:shadow-xl " name="" placeholder="Search models, datasets, users..."   spellcheck="false" type="text" value="">
	<svg class="absolute left-2.5 text-gray-400 top-1/2 transform -translate-y-1/2" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 32 32"><path d="M30 28.59L22.45 21A11 11 0 1 0 21 22.45L28.59 30zM5 14a9 9 0 1 1 9 9a9 9 0 0 1-9-9z" fill="currentColor"></path></svg>
	</div>
			<div class="flex flex-none items-center justify-center p-0.5 place-self-stretch lg:hidden"><button class="relative z-40 flex h-6 w-8 items-center justify-center" type="button"><svg width="1em" height="1em" viewBox="0 0 10 10" class="text-xl" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" preserveAspectRatio="xMidYMid meet" fill="currentColor"><path fill-rule="evenodd" clip-rule="evenodd" d="M1.65039 2.9999C1.65039 2.8066 1.80709 2.6499 2.00039 2.6499H8.00039C8.19369 2.6499 8.35039 2.8066 8.35039 2.9999C8.35039 3.1932 8.19369 3.3499 8.00039 3.3499H2.00039C1.80709 3.3499 1.65039 3.1932 1.65039 2.9999ZM1.65039 4.9999C1.65039 4.8066 1.80709 4.6499 2.00039 4.6499H8.00039C8.19369 4.6499 8.35039 4.8066 8.35039 4.9999C8.35039 5.1932 8.19369 5.3499 8.00039 5.3499H2.00039C1.80709 5.3499 1.65039 5.1932 1.65039 4.9999ZM2.00039 6.6499C1.80709 6.6499 1.65039 6.8066 1.65039 6.9999C1.65039 7.1932 1.80709 7.3499 2.00039 7.3499H8.00039C8.19369 7.3499 8.35039 7.1932 8.35039 6.9999C8.35039 6.8066 8.19369 6.6499 8.00039 6.6499H2.00039Z"></path></svg>
		</button>

	</div></div>
		<nav aria-label="Main" class="ml-auto hidden lg:block"><ul class="flex items-center space-x-1.5 xl:space-x-2"><li><a class="group flex items-center px-2 py-0.5 dark:hover:text-gray-400 hover:text-indigo-700" href="/models"><svg class="mr-1.5 text-gray-400 group-hover:text-indigo-500" style="" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 24 24"><path class="uim-quaternary" d="M20.23 7.24L12 12L3.77 7.24a1.98 1.98 0 0 1 .7-.71L11 2.76c.62-.35 1.38-.35 2 0l6.53 3.77c.29.173.531.418.7.71z" opacity=".25" fill="currentColor"></path><path class="uim-tertiary" d="M12 12v9.5a2.09 2.09 0 0 1-.91-.21L4.5 17.48a2.003 2.003 0 0 1-1-1.73v-7.5a2.06 2.06 0 0 1 .27-1.01L12 12z" opacity=".5" fill="currentColor"></path><path class="uim-primary" d="M20.5 8.25v7.5a2.003 2.003 0 0 1-1 1.73l-6.62 3.82c-.275.13-.576.198-.88.2V12l8.23-4.76c.175.308.268.656.27 1.01z" fill="currentColor"></path></svg>
					Models</a>
			</li><li><a class="group flex items-center px-2 py-0.5 dark:hover:text-gray-400 hover:text-red-700" href="/datasets"><svg class="mr-1.5 text-gray-400 group-hover:text-red-500" style="" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 25 25"><ellipse cx="12.5" cy="5" fill="currentColor" fill-opacity="0.25" rx="7.5" ry="2"></ellipse><path d="M12.5 15C16.6421 15 20 14.1046 20 13V20C20 21.1046 16.6421 22 12.5 22C8.35786 22 5 21.1046 5 20V13C5 14.1046 8.35786 15 12.5 15Z" fill="currentColor" opacity="0.5"></path><path d="M12.5 7C16.6421 7 20 6.10457 20 5V11.5C20 12.6046 16.6421 13.5 12.5 13.5C8.35786 13.5 5 12.6046 5 11.5V5C5 6.10457 8.35786 7 12.5 7Z" fill="currentColor" opacity="0.5"></path><path d="M5.23628 12C5.08204 12.1598 5 12.8273 5 13C5 14.1046 8.35786 15 12.5 15C16.6421 15 20 14.1046 20 13C20 12.8273 19.918 12.1598 19.7637 12C18.9311 12.8626 15.9947 13.5 12.5 13.5C9.0053 13.5 6.06886 12.8626 5.23628 12Z" fill="currentColor"></path></svg>
					Datasets</a>
			</li><li><a class="group flex items-center px-2 py-0.5 dark:hover:text-gray-400 hover:text-blue-700" href="/spaces"><svg class="mr-1.5 text-gray-400 group-hover:text-blue-500" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" viewBox="0 0 25 25"><path opacity=".5" d="M6.016 14.674v4.31h4.31v-4.31h-4.31ZM14.674 14.674v4.31h4.31v-4.31h-4.31ZM6.016 6.016v4.31h4.31v-4.31h-4.31Z" fill="currentColor"></path><path opacity=".75" fill-rule="evenodd" clip-rule="evenodd" d="M3 4.914C3 3.857 3.857 3 4.914 3h6.514c.884 0 1.628.6 1.848 1.414a5.171 5.171 0 0 1 7.31 7.31c.815.22 1.414.964 1.414 1.848v6.514A1.914 1.914 0 0 1 20.086 22H4.914A1.914 1.914 0 0 1 3 20.086V4.914Zm3.016 1.102v4.31h4.31v-4.31h-4.31Zm0 12.968v-4.31h4.31v4.31h-4.31Zm8.658 0v-4.31h4.31v4.31h-4.31Zm0-10.813a2.155 2.155 0 1 1 4.31 0 2.155 2.155 0 0 1-4.31 0Z" fill="currentColor"></path><path opacity=".25" d="M16.829 6.016a2.155 2.155 0 1 0 0 4.31 2.155 2.155 0 0 0 0-4.31Z" fill="currentColor"></path></svg>
					Spaces</a>
			</li><li><a class="group flex items-center px-2 py-0.5 dark:hover:text-gray-400 hover:text-yellow-700" href="/posts"><svg class="mr-1.5 text-gray-400 group-hover:text-yellow-500 !text-yellow-500" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" viewBox="0 0 12 12" preserveAspectRatio="xMidYMid meet"><path fill="currentColor" fill-rule="evenodd" d="M3.73 2.4A4.25 4.25 0 1 1 6 10.26H2.17l-.13-.02a.43.43 0 0 1-.3-.43l.01-.06a.43.43 0 0 1 .12-.22l.84-.84A4.26 4.26 0 0 1 3.73 2.4Z" clip-rule="evenodd"></path></svg>
					Posts</a>
			</li><li><a class="group flex items-center px-2 py-0.5 dark:hover:text-gray-400 hover:text-yellow-700" href="/docs"><svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" role="img" class="mr-1.5 text-gray-400 group-hover:text-yellow-500" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 32 32"><path opacity="0.5" d="M20.9022 5.10334L10.8012 10.8791L7.76318 9.11193C8.07741 8.56791 8.5256 8.11332 9.06512 7.7914L15.9336 3.73907C17.0868 3.08811 18.5002 3.26422 19.6534 3.91519L19.3859 3.73911C19.9253 4.06087 20.5879 4.56025 20.9022 5.10334Z" fill="currentColor"></path><path d="M10.7999 10.8792V28.5483C10.2136 28.5475 9.63494 28.4139 9.10745 28.1578C8.5429 27.8312 8.074 27.3621 7.74761 26.7975C7.42122 26.2327 7.24878 25.5923 7.24756 24.9402V10.9908C7.25062 10.3319 7.42358 9.68487 7.74973 9.1123L10.7999 10.8792Z" fill="currentColor" fill-opacity="0.75"></path><path fill-rule="evenodd" clip-rule="evenodd" d="M21.3368 10.8499V6.918C21.3331 6.25959 21.16 5.61234 20.8346 5.03949L10.7971 10.8727L10.8046 10.874L21.3368 10.8499Z" fill="currentColor"></path><path opacity="0.5" d="M21.7937 10.8488L10.7825 10.8741V28.5486L21.7937 28.5234C23.3344 28.5234 24.5835 27.2743 24.5835 25.7335V13.6387C24.5835 12.0979 23.4365 11.1233 21.7937 10.8488Z" fill="currentColor"></path></svg>
					Docs</a>
			</li>
		<li class="max-2xl:hidden"><div class="relative ">
	<button class="px-2 py-0.5 group hover:text-green-700 dark:hover:text-gray-400 flex items-center " type="button">
		<svg class="mr-1.5 text-gray-400 group-hover:text-green-500" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 24 24"><path class="uim-tertiary" d="M19 6H5a3 3 0 0 0-3 3v2.72L8.837 14h6.326L22 11.72V9a3 3 0 0 0-3-3z" opacity=".5" fill="currentColor"></path><path class="uim-primary" d="M10 6V5h4v1h2V5a2.002 2.002 0 0 0-2-2h-4a2.002 2.002 0 0 0-2 2v1h2zm-1.163 8L2 11.72V18a3.003 3.003 0 0 0 3 3h14a3.003 3.003 0 0 0 3-3v-6.28L15.163 14H8.837z" fill="currentColor"></path></svg>
			Solutions
		</button>
	
	
	</div></li>
		<li><a class="group flex items-center px-2 py-0.5 hover:text-gray-500 dark:hover:text-gray-400" href="/pricing">Pricing
			</a></li>

		<li><div class="relative group">
	<button class="px-2 py-0.5 hover:text-gray-500 dark:hover:text-gray-600 flex items-center " type="button">
		<svg class=" text-gray-500 w-5 group-hover:text-gray-400 dark:text-gray-300 dark:group-hover:text-gray-400" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" viewBox="0 0 32 18" preserveAspectRatio="xMidYMid meet"><path fill-rule="evenodd" clip-rule="evenodd" d="M14.4504 3.30221C14.4504 2.836 14.8284 2.45807 15.2946 2.45807H28.4933C28.9595 2.45807 29.3374 2.836 29.3374 3.30221C29.3374 3.76842 28.9595 4.14635 28.4933 4.14635H15.2946C14.8284 4.14635 14.4504 3.76842 14.4504 3.30221Z" fill="currentColor"></path><path fill-rule="evenodd" clip-rule="evenodd" d="M14.4504 9.00002C14.4504 8.53382 14.8284 8.15588 15.2946 8.15588H28.4933C28.9595 8.15588 29.3374 8.53382 29.3374 9.00002C29.3374 9.46623 28.9595 9.84417 28.4933 9.84417H15.2946C14.8284 9.84417 14.4504 9.46623 14.4504 9.00002Z" fill="currentColor"></path><path fill-rule="evenodd" clip-rule="evenodd" d="M14.4504 14.6978C14.4504 14.2316 14.8284 13.8537 15.2946 13.8537H28.4933C28.9595 13.8537 29.3374 14.2316 29.3374 14.6978C29.3374 15.164 28.9595 15.542 28.4933 15.542H15.2946C14.8284 15.542 14.4504 15.164 14.4504 14.6978Z" fill="currentColor"></path><path fill-rule="evenodd" clip-rule="evenodd" d="M1.94549 6.87377C2.27514 6.54411 2.80962 6.54411 3.13928 6.87377L6.23458 9.96907L9.32988 6.87377C9.65954 6.54411 10.194 6.54411 10.5237 6.87377C10.8533 7.20343 10.8533 7.73791 10.5237 8.06756L6.23458 12.3567L1.94549 8.06756C1.61583 7.73791 1.61583 7.20343 1.94549 6.87377Z" fill="currentColor"></path></svg>
			
		</button>
	
	
	</div></li>
		<li><hr class="h-5 w-0.5 border-none bg-gray-100 dark:bg-gray-800"></li>
		<li><form action="/logout" method="POST" class="hidden"><input type="hidden" name="csrf" value="eyJkYXRhIjp7ImV4cGlyYXRpb24iOjE3MzA4Nzg1NDY1NDgsInVzZXJJZCI6IjY2YjIxYTA4ZGYxZTUzODMxZTAwYmVkMyJ9LCJzaWduYXR1cmUiOiIyMzE1ZDhlNmE4MjI1NzViZDM0ZDE1YjUyOGE0OTc2NmQ4NGZjNzI3YTE4YzhkMDQzNzMzMzkzMTcxMzQwMTc4In0="></form>
<div class="relative ml-2 w-[1.38rem] h-[1.38rem] ">
	<button class="ml-auto rounded-full ring-2 group ring-indigo-400 focus:ring-blue-500 hover:ring-offset-1 focus:ring-offset-1 focus:outline-none outline-none dark:ring-offset-gray-950 " type="button">
		
		<div class="relative"><img alt="" class="h-[1.38rem] w-[1.38rem] overflow-hidden rounded-full" src="/avatars/c36a740672ff0acce1d7d9f6dbb97b46.svg" crossorigin="anonymous">
			</div>
	
		</button>
	
	
	</div></li></ul></nav></div></header></div>
	
	
	
	<div class="SVELTE_HYDRATER contents" data-target="SSOBanner" data-props="{&quot;organizations&quot;:[]}"></div>
	
	

	<main class="flex flex-1 flex-col"><div class="SVELTE_HYDRATER contents" data-target="SpaceHeader" data-props="{&quot;activeTab&quot;:&quot;files&quot;,&quot;authLight&quot;:{&quot;csrfToken&quot;:&quot;eyJkYXRhIjp7ImV4cGlyYXRpb24iOjE3MzA4Nzg1NDY1NDgsInVzZXJJZCI6IjY2YjIxYTA4ZGYxZTUzODMxZTAwYmVkMyJ9LCJzaWduYXR1cmUiOiIyMzE1ZDhlNmE4MjI1NzViZDM0ZDE1YjUyOGE0OTc2NmQ4NGZjNzI3YTE4YzhkMDQzNzMzMzkzMTcxMzQwMTc4In0=&quot;,&quot;hasHfLevelAccess&quot;:false,&quot;u&quot;:{&quot;avatarUrl&quot;:&quot;/avatars/c36a740672ff0acce1d7d9f6dbb97b46.svg&quot;,&quot;isPro&quot;:false,&quot;orgs&quot;:[],&quot;user&quot;:&quot;ghstmnnn&quot;,&quot;canPost&quot;:false,&quot;canHaveBilling&quot;:true,&quot;canCreateOrg&quot;:true,&quot;theme&quot;:&quot;light&quot;,&quot;notifications&quot;:{&quot;org_suggestions&quot;:false}}},&quot;author&quot;:{&quot;avatarUrl&quot;:&quot;https://cdn-avatars.huggingface.co/v1/production/uploads/637c3504c292c0fd3f37361f/wyTkbYKi8HufRT65LGN0P.jpeg&quot;,&quot;fullname&quot;:&quot;seungheon.doh&quot;,&quot;name&quot;:&quot;seungheondoh&quot;,&quot;type&quot;:&quot;user&quot;,&quot;isPro&quot;:false,&quot;isHf&quot;:false,&quot;isMod&quot;:false,&quot;followerCount&quot;:28},&quot;canDisable&quot;:false,&quot;canReadRepoSettings&quot;:false,&quot;canWriteRepoSettings&quot;:false,&quot;discussionsStats&quot;:{&quot;closed&quot;:0,&quot;open&quot;:1,&quot;total&quot;:1},&quot;query&quot;:{},&quot;space&quot;:{&quot;author&quot;:&quot;seungheondoh&quot;,&quot;colorFrom&quot;:&quot;purple&quot;,&quot;colorTo&quot;:&quot;indigo&quot;,&quot;cardData&quot;:{&quot;title&quot;:&quot;Lp Music Caps&quot;,&quot;emoji&quot;:&quot;🎵🎵🎵&quot;,&quot;colorFrom&quot;:&quot;purple&quot;,&quot;colorTo&quot;:&quot;indigo&quot;,&quot;sdk&quot;:&quot;gradio&quot;,&quot;sdk_version&quot;:&quot;3.33.1&quot;,&quot;app_file&quot;:&quot;app.py&quot;,&quot;pinned&quot;:false,&quot;license&quot;:&quot;mit&quot;},&quot;createdAt&quot;:&quot;2023-07-10T08:00:26.000Z&quot;,&quot;emoji&quot;:&quot;🎵🎵🎵&quot;,&quot;discussionsDisabled&quot;:false,&quot;duplicationDisabled&quot;:false,&quot;id&quot;:&quot;seungheondoh/LP-Music-Caps-demo&quot;,&quot;isLikedByUser&quot;:true,&quot;watched&quot;:{&quot;isWatching&quot;:false,&quot;isMuted&quot;:false,&quot;mode&quot;:&quot;none&quot;},&quot;lastModified&quot;:&quot;2023-10-23T05:23:02.000Z&quot;,&quot;likes&quot;:153,&quot;pinned&quot;:false,&quot;private&quot;:false,&quot;gated&quot;:false,&quot;repoType&quot;:&quot;space&quot;,&quot;subdomain&quot;:&quot;seungheondoh-lp-music-caps-demo&quot;,&quot;sdk&quot;:&quot;gradio&quot;,&quot;sdkVersion&quot;:&quot;3.33.1&quot;,&quot;title&quot;:&quot;Lp Music Caps&quot;,&quot;runtime&quot;:{&quot;stage&quot;:&quot;RUNNING&quot;,&quot;hardware&quot;:{&quot;current&quot;:&quot;cpu-basic&quot;,&quot;requested&quot;:&quot;cpu-basic&quot;},&quot;storage&quot;:null,&quot;gcTimeout&quot;:86400,&quot;replicas&quot;:{&quot;current&quot;:1,&quot;requested&quot;:1},&quot;devMode&quot;:false,&quot;domains&quot;:[{&quot;domain&quot;:&quot;seungheondoh-lp-music-caps-demo.hf.space&quot;,&quot;isCustom&quot;:false,&quot;stage&quot;:&quot;READY&quot;}],&quot;sha&quot;:&quot;83027ae8b0806281fa539ebf43f69b016265bcee&quot;},&quot;iframe&quot;:{&quot;embedSrc&quot;:&quot;https://seungheondoh-lp-music-caps-demo.hf.space&quot;,&quot;src&quot;:&quot;https://seungheondoh-lp-music-caps-demo.hf.space&quot;},&quot;secrets&quot;:[],&quot;variables&quot;:[],&quot;sse&quot;:{&quot;url&quot;:&quot;https://api.hf.space/v1/seungheondoh/LP-Music-Caps-demo&quot;,&quot;jwt&quot;:&quot;eyJhbGciOiJFZERTQSJ9.eyJyZWFkIjp0cnVlLCJwZXJtaXNzaW9ucyI6eyJyZXBvLmNvbnRlbnQucmVhZCI6dHJ1ZX0sIm9uQmVoYWxmT2YiOnsia2luZCI6InVzZXIiLCJfaWQiOiI2NmIyMWEwOGRmMWU1MzgzMWUwMGJlZDMiLCJ1c2VyIjoiZ2hzdG1ubm4ifSwiaWF0IjoxNzMwNzkyMTQ2LCJzdWIiOiIvc3BhY2VzL3NldW5naGVvbmRvaC9MUC1NdXNpYy1DYXBzLWRlbW8iLCJleHAiOjE3MzA4Nzg1NDYsImlzcyI6Imh0dHBzOi8vaHVnZ2luZ2ZhY2UuY28ifQ.13PrivuGpVXIlU_oYsq1kT0pn3Q-mWN7R_wFwrmfrPt3kd5kRmfod2YG9NLys8YsAQ1nKKN0SKIGrnNJA5kFCw&quot;},&quot;linkedModels&quot;:[{&quot;author&quot;:&quot;facebook&quot;,&quot;authorData&quot;:{&quot;avatarUrl&quot;:&quot;https://cdn-avatars.huggingface.co/v1/production/uploads/1592839207516-noauth.png&quot;,&quot;fullname&quot;:&quot;AI at Meta&quot;,&quot;name&quot;:&quot;facebook&quot;,&quot;type&quot;:&quot;org&quot;,&quot;isHf&quot;:false,&quot;isMod&quot;:false,&quot;isEnterprise&quot;:true,&quot;followerCount&quot;:3249},&quot;downloads&quot;:3337790,&quot;gated&quot;:false,&quot;id&quot;:&quot;facebook/bart-base&quot;,&quot;inference&quot;:&quot;cold&quot;,&quot;lastModified&quot;:&quot;2022-11-16T23:23:10.000Z&quot;,&quot;likes&quot;:166,&quot;pipeline_tag&quot;:&quot;feature-extraction&quot;,&quot;private&quot;:false,&quot;repoType&quot;:&quot;model&quot;,&quot;isLikedByUser&quot;:false},{&quot;author&quot;:&quot;seungheondoh&quot;,&quot;authorData&quot;:{&quot;avatarUrl&quot;:&quot;https://cdn-avatars.huggingface.co/v1/production/uploads/637c3504c292c0fd3f37361f/wyTkbYKi8HufRT65LGN0P.jpeg&quot;,&quot;fullname&quot;:&quot;seungheon.doh&quot;,&quot;name&quot;:&quot;seungheondoh&quot;,&quot;type&quot;:&quot;user&quot;,&quot;isPro&quot;:false,&quot;isHf&quot;:false,&quot;isMod&quot;:false,&quot;followerCount&quot;:28},&quot;downloads&quot;:0,&quot;gated&quot;:false,&quot;id&quot;:&quot;seungheondoh/lp-music-caps&quot;,&quot;inference&quot;:&quot;library-not-detected&quot;,&quot;lastModified&quot;:&quot;2023-08-01T04:06:07.000Z&quot;,&quot;likes&quot;:17,&quot;private&quot;:false,&quot;repoType&quot;:&quot;model&quot;,&quot;isLikedByUser&quot;:false}],&quot;linkedDatasets&quot;:[{&quot;author&quot;:&quot;seungheondoh&quot;,&quot;downloads&quot;:114,&quot;gated&quot;:false,&quot;id&quot;:&quot;seungheondoh/LP-MusicCaps-MC&quot;,&quot;lastModified&quot;:&quot;2023-08-01T03:52:24.000Z&quot;,&quot;datasetsServerInfo&quot;:{&quot;viewer&quot;:&quot;viewer&quot;,&quot;numRows&quot;:5521,&quot;libraries&quot;:[&quot;datasets&quot;,&quot;pandas&quot;,&quot;mlcroissant&quot;,&quot;polars&quot;],&quot;formats&quot;:[&quot;parquet&quot;],&quot;modalities&quot;:[&quot;tabular&quot;,&quot;text&quot;]},&quot;private&quot;:false,&quot;repoType&quot;:&quot;dataset&quot;,&quot;likes&quot;:9,&quot;isLikedByUser&quot;:false}],&quot;linkedCollections&quot;:[],&quot;sha&quot;:&quot;83027ae8b0806281fa539ebf43f69b016265bcee&quot;,&quot;hasBlockedOids&quot;:false},&quot;u&quot;:{&quot;avatarUrl&quot;:&quot;/avatars/c36a740672ff0acce1d7d9f6dbb97b46.svg&quot;,&quot;isPro&quot;:false,&quot;fullname&quot;:&quot;pok&quot;,&quot;user&quot;:&quot;ghstmnnn&quot;,&quot;orgs&quot;:[],&quot;signup&quot;:{},&quot;isHf&quot;:false,&quot;isMod&quot;:false,&quot;type&quot;:&quot;user&quot;,&quot;canPay&quot;:false,&quot;spacesAvailableFlavors&quot;:[&quot;cpu-basic&quot;,&quot;zero-a10g&quot;,&quot;cpu-upgrade&quot;,&quot;t4-small&quot;,&quot;t4-medium&quot;,&quot;l4x1&quot;,&quot;l4x4&quot;,&quot;l40sx1&quot;,&quot;l40sx4&quot;,&quot;l40sx8&quot;,&quot;a10g-small&quot;,&quot;a10g-large&quot;,&quot;a10g-largex2&quot;,&quot;a10g-largex4&quot;,&quot;a100-large&quot;,&quot;v5e-1x1&quot;,&quot;v5e-2x2&quot;,&quot;v5e-2x4&quot;],&quot;canPost&quot;:false}}">

<header class="from-gray-50-to-white border-b border-gray-100 bg-gradient-to-t via-white dark:via-gray-950 pt-4 xl:pt-0"><div class="container relative flex flex-col xl:flex-row"><h1 class="flex flex-wrap items-center leading-tight gap-y-1 text-lg xl:flex-none"><a href="/spaces" class="group flex items-center"><svg class="mr-1 text-gray-400" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 32 32"><path d="M7.80914 18.7462V24.1907H13.2536V18.7462H7.80914Z" fill="#FF3270"></path><path d="M18.7458 18.7462V24.1907H24.1903V18.7462H18.7458Z" fill="#861FFF"></path><path d="M7.80914 7.80982V13.2543H13.2536V7.80982H7.80914Z" fill="#097EFF"></path><path fill-rule="evenodd" clip-rule="evenodd" d="M4 6.41775C4 5.08246 5.08246 4 6.41775 4H14.6457C15.7626 4 16.7026 4.75724 16.9802 5.78629C18.1505 4.67902 19.7302 4 21.4685 4C25.0758 4 28.0003 6.92436 28.0003 10.5317C28.0003 12.27 27.3212 13.8497 26.2139 15.02C27.243 15.2977 28.0003 16.2376 28.0003 17.3545V25.5824C28.0003 26.9177 26.9177 28.0003 25.5824 28.0003H17.0635H14.9367H6.41775C5.08246 28.0003 4 26.9177 4 25.5824V15.1587V14.9367V6.41775ZM7.80952 7.80952V13.254H13.254V7.80952H7.80952ZM7.80952 24.1907V18.7462H13.254V24.1907H7.80952ZM18.7462 24.1907V18.7462H24.1907V24.1907H18.7462ZM18.7462 10.5317C18.7462 9.0283 19.9651 7.80952 21.4685 7.80952C22.9719 7.80952 24.1907 9.0283 24.1907 10.5317C24.1907 12.0352 22.9719 13.254 21.4685 13.254C19.9651 13.254 18.7462 12.0352 18.7462 10.5317Z" fill="black"></path><path d="M21.4681 7.80982C19.9647 7.80982 18.7458 9.02861 18.7458 10.5321C18.7458 12.0355 19.9647 13.2543 21.4681 13.2543C22.9715 13.2543 24.1903 12.0355 24.1903 10.5321C24.1903 9.02861 22.9715 7.80982 21.4681 7.80982Z" fill="#FFD702"></path></svg>
					<span class="mr-2.5 font-semibold text-gray-400 group-hover:text-gray-500">Spaces:</span></a>
			<div class="group flex flex-none items-center"><div class="relative mr-1 flex items-center">

			<img alt="" class="w-3.5 h-3.5 rounded-full  flex-none" src="https://cdn-avatars.huggingface.co/v1/production/uploads/637c3504c292c0fd3f37361f/wyTkbYKi8HufRT65LGN0P.jpeg" crossorigin="anonymous"></div>
		<a href="/seungheondoh" class="text-gray-400 hover:text-blue-600">seungheondoh</a>
		<div class="mx-0.5 text-gray-300">/</div></div>

<div class="max-w-full xl:flex xl:min-w-0 xl:flex-nowrap xl:items-center xl:gap-x-1"><a class="break-words font-mono font-semibold hover:text-blue-600 text-[1.07rem] xl:truncate" href="/spaces/seungheondoh/LP-Music-Caps-demo">LP-Music-Caps-demo</a>
	<button class="relative text-xs mr-3  inline-flex cursor-pointer items-center text-sm focus:outline-none  mx-0.5   text-gray-600 " title="Copy space name to clipboard" type="button"><svg class="" xmlns="http://www.w3.org/2000/svg" aria-hidden="true" fill="currentColor" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 32 32"><path d="M28,10V28H10V10H28m0-2H10a2,2,0,0,0-2,2V28a2,2,0,0,0,2,2H28a2,2,0,0,0,2-2V10a2,2,0,0,0-2-2Z" transform="translate(0)"></path><path d="M4,18H2V4A2,2,0,0,1,4,2H18V4H4Z" transform="translate(0)"></path><rect fill="none" width="32" height="32"></rect></svg>
	
	</button></div>
			<div class="inline-flex items-center overflow-hidden whitespace-nowrap rounded-md border bg-white text-sm leading-none text-gray-500  mr-2"><button class="relative flex items-center overflow-hidden from-red-50 to-transparent dark:from-red-900 px-1.5 py-1 hover:bg-gradient-to-t focus:outline-none"  title="Unlike"><svg class="left-1.5 absolute" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 32 32" fill="currentColor"><path d="M22.45,6a5.47,5.47,0,0,1,3.91,1.64,5.7,5.7,0,0,1,0,8L16,26.13,5.64,15.64a5.7,5.7,0,0,1,0-8,5.48,5.48,0,0,1,7.82,0L16,10.24l2.53-2.58A5.44,5.44,0,0,1,22.45,6m0-2a7.47,7.47,0,0,0-5.34,2.24L16,7.36,14.89,6.24a7.49,7.49,0,0,0-10.68,0,7.72,7.72,0,0,0,0,10.82L16,29,27.79,17.06a7.72,7.72,0,0,0,0-10.82A7.49,7.49,0,0,0,22.45,4Z"></path></svg>

		<svg class="absolute text-red-500 origin-center transform transition-transform ease-in
						
						left-1.5 " xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 32 32" fill="currentColor"><path d="M22.5,4c-2,0-3.9,0.8-5.3,2.2L16,7.4l-1.1-1.1C12,3.3,7.2,3.3,4.3,6.2c0,0-0.1,0.1-0.1,0.1c-3,3-3,7.8,0,10.8L16,29l11.8-11.9c3-3,3-7.8,0-10.8C26.4,4.8,24.5,4,22.5,4z"></path></svg>
		<span class="ml-4 pl-0.5 ">like</span></button>
	<button class="flex items-center border-l px-1.5 py-1 text-gray-400 hover:bg-gray-50 focus:bg-gray-100 focus:outline-none dark:hover:bg-gray-900 dark:focus:bg-gray-800" title="See users who liked this repository">153</button></div>




			
			



<span class="inline-block "><span class="contents"><div class="inline-flex cursor-pointer select-none items-center overflow-hidden font-mono text-xs flex-shrink-0 mr-2 rounded-lg border leading-none dark:bg-gray-900
					border-green-100 
					text-green-700 dark:text-green-500"><div class="inline-flex items-center px-2 py-[0.32rem] dark:bg-gray-900  border-green-100 bg-green-50 hover:bg-green-100/70 hover:text-green-800 dark:hover:text-green-400">
					<div class="ml-0.5 mr-1.5 inline-block h-1.5 w-1.5 animate-pulse rounded-full bg-green-500"></div>
		Running
		</div>
	</div></span>

	</span>

	


			
			

<div class="sm:hidden"><div class="relative ">
	<button class="btn px-1 py-1 text-sm translate-y-0 " type="button">
		
			<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" role="img" class="p-px" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 32 32"><circle cx="16" cy="7" r="3" fill="currentColor"></circle><circle cx="16" cy="16" r="3" fill="currentColor"></circle><circle cx="16" cy="25" r="3" fill="currentColor"></circle></svg>
			<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" class="absolute right-[-0.25rem] bottom-[-0.25rem]  rounded-sm bg-gray-50 p-px text-[0.85rem] text-gray-500 dark:bg-gray-925" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 12 12"><path fill="currentColor" d="M7.975 3.489a.438.438 0 0 1 0 .618L4.262 7.82a.416.416 0 0 1-.307.126.427.427 0 0 1-.311-.126.438.438 0 0 1 0-.618L7.357 3.49a.438.438 0 0 1 .618 0ZM6.427 8.132 4.88 9.675a2.17 2.17 0 0 1-3.09 0 2.188 2.188 0 0 1 0-3.09l1.542-1.548a.437.437 0 0 0-.618-.619L1.166 5.966a3.063 3.063 0 0 0 4.332 4.332L7.046 8.75a.438.438 0 0 0-.619-.618Zm4.026-7.121a3.063 3.063 0 0 0-4.332 0L4.573 2.559a.438.438 0 0 0 .618.618L6.74 1.635a2.171 2.171 0 0 1 3.09 0 2.188 2.188 0 0 1 0 3.09L8.287 6.273a.432.432 0 0 0 0 .618.421.421 0 0 0 .475.097.438.438 0 0 0 .143-.097l1.548-1.548a3.068 3.068 0 0 0 0-4.332Z"></path></svg>
		
		</button>
	
	
	</div></div>





</h1>
		

		<div class="flex flex-col-reverse gap-x-2 sm:flex-row sm:items-center sm:justify-between xl:ml-auto"><div class="-mb-px flex h-12 items-center overflow-x-auto overflow-y-hidden sm:h-[3.25rem]"><a class="tab-alternate " href="/spaces/seungheondoh/LP-Music-Caps-demo"><svg class="mr-1.5 text-gray-400 flex-none" style="" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 24 24"><path class="uim-quaternary" d="M20.23 7.24L12 12L3.77 7.24a1.98 1.98 0 0 1 .7-.71L11 2.76c.62-.35 1.38-.35 2 0l6.53 3.77c.29.173.531.418.7.71z" opacity=".25" fill="currentColor"></path><path class="uim-tertiary" d="M12 12v9.5a2.09 2.09 0 0 1-.91-.21L4.5 17.48a2.003 2.003 0 0 1-1-1.73v-7.5a2.06 2.06 0 0 1 .27-1.01L12 12z" opacity=".5" fill="currentColor"></path><path class="uim-primary" d="M20.5 8.25v7.5a2.003 2.003 0 0 1-1 1.73l-6.62 3.82c-.275.13-.576.198-.88.2V12l8.23-4.76c.175.308.268.656.27 1.01z" fill="currentColor"></path></svg>
			App
			
			
		</a><a class="tab-alternate active" href="/spaces/seungheondoh/LP-Music-Caps-demo/tree/main"><svg class="mr-1.5 text-gray-400 flex-none" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 24 24"><path class="uim-tertiary" d="M21 19h-8a1 1 0 0 1 0-2h8a1 1 0 0 1 0 2zm0-4h-8a1 1 0 0 1 0-2h8a1 1 0 0 1 0 2zm0-8h-8a1 1 0 0 1 0-2h8a1 1 0 0 1 0 2zm0 4h-8a1 1 0 0 1 0-2h8a1 1 0 0 1 0 2z" opacity=".5" fill="currentColor"></path><path class="uim-primary" d="M9 19a1 1 0 0 1-1-1V6a1 1 0 0 1 2 0v12a1 1 0 0 1-1 1zm-6-4.333a1 1 0 0 1-.64-1.769L3.438 12l-1.078-.898a1 1 0 0 1 1.28-1.538l2 1.667a1 1 0 0 1 0 1.538l-2 1.667a.999.999 0 0 1-.64.231z" fill="currentColor"></path></svg>
			<span class="xl:hidden">Files</span>
				<span class="hidden xl:inline">Files</span>
			
			
		</a><a class="tab-alternate " href="/spaces/seungheondoh/LP-Music-Caps-demo/discussions"><svg class="mr-1.5 text-gray-400 flex-none" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 32 32"><path d="M20.6081 3C21.7684 3 22.8053 3.49196 23.5284 4.38415C23.9756 4.93678 24.4428 5.82749 24.4808 7.16133C24.9674 7.01707 25.4353 6.93643 25.8725 6.93643C26.9833 6.93643 27.9865 7.37587 28.696 8.17411C29.6075 9.19872 30.0124 10.4579 29.8361 11.7177C29.7523 12.3177 29.5581 12.8555 29.2678 13.3534C29.8798 13.8646 30.3306 14.5763 30.5485 15.4322C30.719 16.1032 30.8939 17.5006 29.9808 18.9403C30.0389 19.0342 30.0934 19.1319 30.1442 19.2318C30.6932 20.3074 30.7283 21.5229 30.2439 22.6548C29.5093 24.3704 27.6841 25.7219 24.1397 27.1727C21.9347 28.0753 19.9174 28.6523 19.8994 28.6575C16.9842 29.4379 14.3477 29.8345 12.0653 29.8345C7.87017 29.8345 4.8668 28.508 3.13831 25.8921C0.356375 21.6797 0.754104 17.8269 4.35369 14.1131C6.34591 12.058 7.67023 9.02782 7.94613 8.36275C8.50224 6.39343 9.97271 4.20438 12.4172 4.20438H12.4179C12.6236 4.20438 12.8314 4.2214 13.0364 4.25468C14.107 4.42854 15.0428 5.06476 15.7115 6.02205C16.4331 5.09583 17.134 4.359 17.7682 3.94323C18.7242 3.31737 19.6794 3 20.6081 3ZM20.6081 5.95917C20.2427 5.95917 19.7963 6.1197 19.3039 6.44225C17.7754 7.44319 14.8258 12.6772 13.7458 14.7131C13.3839 15.3952 12.7655 15.6837 12.2086 15.6837C11.1036 15.6837 10.2408 14.5497 12.1076 13.1085C14.9146 10.9402 13.9299 7.39584 12.5898 7.1776C12.5311 7.16799 12.4731 7.16355 12.4172 7.16355C11.1989 7.16355 10.6615 9.33114 10.6615 9.33114C10.6615 9.33114 9.0863 13.4148 6.38031 16.206C3.67434 18.998 3.5346 21.2388 5.50675 24.2246C6.85185 26.2606 9.42666 26.8753 12.0653 26.8753C14.8021 26.8753 17.6077 26.2139 19.1799 25.793C19.2574 25.7723 28.8193 22.984 27.6081 20.6107C27.4046 20.212 27.0693 20.0522 26.6471 20.0522C24.9416 20.0522 21.8393 22.6726 20.5057 22.6726C20.2076 22.6726 19.9976 22.5416 19.9116 22.222C19.3433 20.1173 28.552 19.2325 27.7758 16.1839C27.639 15.6445 27.2677 15.4256 26.746 15.4263C24.4923 15.4263 19.4358 19.5181 18.3759 19.5181C18.2949 19.5181 18.2368 19.4937 18.2053 19.4419C17.6743 18.557 17.9653 17.9394 21.7082 15.6009C25.4511 13.2617 28.0783 11.8545 26.5841 10.1752C26.4121 9.98141 26.1684 9.8956 25.8725 9.8956C23.6001 9.89634 18.2311 14.9403 18.2311 14.9403C18.2311 14.9403 16.7821 16.496 15.9057 16.496C15.7043 16.496 15.533 16.4139 15.4169 16.2112C14.7956 15.1296 21.1879 10.1286 21.5484 8.06535C21.7928 6.66715 21.3771 5.95917 20.6081 5.95917Z" fill="#FF9D00"></path><path d="M5.50686 24.2246C3.53472 21.2387 3.67446 18.9979 6.38043 16.206C9.08641 13.4147 10.6615 9.33111 10.6615 9.33111C10.6615 9.33111 11.2499 6.95933 12.59 7.17757C13.93 7.39581 14.9139 10.9401 12.1069 13.1084C9.29997 15.276 12.6659 16.7489 13.7459 14.713C14.8258 12.6772 17.7747 7.44316 19.304 6.44221C20.8326 5.44128 21.9089 6.00204 21.5484 8.06532C21.188 10.1286 14.795 15.1295 15.4171 16.2118C16.0391 17.2934 18.2312 14.9402 18.2312 14.9402C18.2312 14.9402 25.0907 8.49588 26.5842 10.1752C28.0776 11.8545 25.4512 13.2616 21.7082 15.6008C17.9646 17.9393 17.6744 18.557 18.2054 19.4418C18.7372 20.3266 26.9998 13.1351 27.7759 16.1838C28.5513 19.2324 19.3434 20.1173 19.9117 22.2219C20.48 24.3274 26.3979 18.2382 27.6082 20.6107C28.8193 22.9839 19.2574 25.7722 19.18 25.7929C16.0914 26.62 8.24723 28.3726 5.50686 24.2246Z" fill="#FFD21E"></path></svg>
			Community
			<div class="ml-1.5 flex h-4 min-w-[1rem] items-center justify-center rounded px-1 text-xs leading-none shadow-sm bg-black text-white dark:bg-gray-800 dark:text-gray-200">1
				</div>
			
		</a>
	</div>
		
			

<div class="hidden sm:block mt-2 lg:mt-0"><div class="relative ">
	<button class="btn px-1 py-1 text-base translate-y-px " type="button">
		
			<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" role="img" class="p-0.5" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 32 32"><circle cx="16" cy="7" r="3" fill="currentColor"></circle><circle cx="16" cy="16" r="3" fill="currentColor"></circle><circle cx="16" cy="25" r="3" fill="currentColor"></circle></svg>
			<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" class="absolute right-[-0.18rem] bottom-[-0.18rem]  rounded-sm bg-gray-50 p-px text-[0.85rem] text-gray-500 dark:bg-gray-925" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 12 12"><path fill="currentColor" d="M7.975 3.489a.438.438 0 0 1 0 .618L4.262 7.82a.416.416 0 0 1-.307.126.427.427 0 0 1-.311-.126.438.438 0 0 1 0-.618L7.357 3.49a.438.438 0 0 1 .618 0ZM6.427 8.132 4.88 9.675a2.17 2.17 0 0 1-3.09 0 2.188 2.188 0 0 1 0-3.09l1.542-1.548a.437.437 0 0 0-.618-.619L1.166 5.966a3.063 3.063 0 0 0 4.332 4.332L7.046 8.75a.438.438 0 0 0-.619-.618Zm4.026-7.121a3.063 3.063 0 0 0-4.332 0L4.573 2.559a.438.438 0 0 0 .618.618L6.74 1.635a2.171 2.171 0 0 1 3.09 0 2.188 2.188 0 0 1 0 3.09L8.287 6.273a.432.432 0 0 0 0 .618.421.421 0 0 0 .475.097.438.438 0 0 0 .143-.097l1.548-1.548a3.068 3.068 0 0 0 0-4.332Z"></path></svg>
		
		</button>
	
	
	</div></div>






		</div></div></header>


























	



</div>
	
<div class="container relative flex flex-col md:grid md:space-y-0 w-full md:grid-cols-12  space-y-4 md:gap-6 mb-16"><section class="pt-8 border-gray-100 col-span-full"><header class="flex flex-wrap items-center justify-start pb-2 md:justify-end lg:flex-nowrap"><div class="relative mr-4 flex min-w-0 basis-auto flex-wrap items-center md:flex-grow md:basis-full lg:basis-auto lg:flex-nowrap"><div class="SVELTE_HYDRATER contents" data-target="BranchSelector" data-props="{&quot;path&quot;:&quot;utils/audio_utils.py&quot;,&quot;repoName&quot;:&quot;seungheondoh/LP-Music-Caps-demo&quot;,&quot;repoType&quot;:&quot;space&quot;,&quot;rev&quot;:&quot;main&quot;,&quot;refs&quot;:{&quot;branches&quot;:[{&quot;name&quot;:&quot;main&quot;,&quot;ref&quot;:&quot;refs/heads/main&quot;,&quot;targetCommit&quot;:&quot;83027ae8b0806281fa539ebf43f69b016265bcee&quot;}],&quot;tags&quot;:[],&quot;converts&quot;:[]},&quot;view&quot;:&quot;blob&quot;}"><div class="relative mr-4 mb-2">
	<button class="text-sm md:text-base btn w-full cursor-pointer text-sm" type="button">
		<svg class="mr-1.5 text-gray-700 dark:text-gray-400" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 24 24" style="transform: rotate(360deg);"><path d="M13 14c-3.36 0-4.46 1.35-4.82 2.24C9.25 16.7 10 17.76 10 19a3 3 0 0 1-3 3a3 3 0 0 1-3-3c0-1.31.83-2.42 2-2.83V7.83A2.99 2.99 0 0 1 4 5a3 3 0 0 1 3-3a3 3 0 0 1 3 3c0 1.31-.83 2.42-2 2.83v5.29c.88-.65 2.16-1.12 4-1.12c2.67 0 3.56-1.34 3.85-2.23A3.006 3.006 0 0 1 14 7a3 3 0 0 1 3-3a3 3 0 0 1 3 3c0 1.34-.88 2.5-2.09 2.86C17.65 11.29 16.68 14 13 14m-6 4a1 1 0 0 0-1 1a1 1 0 0 0 1 1a1 1 0 0 0 1-1a1 1 0 0 0-1-1M7 4a1 1 0 0 0-1 1a1 1 0 0 0 1 1a1 1 0 0 0 1-1a1 1 0 0 0-1-1m10 2a1 1 0 0 0-1 1a1 1 0 0 0 1 1a1 1 0 0 0 1-1a1 1 0 0 0-1-1z" fill="currentColor"></path></svg>
			main
		<svg class="-mr-1 text-gray-500" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 24 24"><path d="M16.293 9.293L12 13.586L7.707 9.293l-1.414 1.414L12 16.414l5.707-5.707z" fill="currentColor"></path></svg></button>
	
	
	</div></div>
		<div class="relative mb-2 flex flex-wrap items-center"><a class="truncate text-gray-800 hover:underline" href="/spaces/seungheondoh/LP-Music-Caps-demo/tree/main">LP-Music-Caps-demo</a>
			<span class="mx-1 text-gray-300">/</span>
				<a class="truncate hover:underline dark:text-gray-300" href="/spaces/seungheondoh/LP-Music-Caps-demo/tree/main/utils">utils
							</a>
						<span class="mx-1 text-gray-300">/</span><span class="dark:text-gray-300">audio_utils.py</span>
				<div class="SVELTE_HYDRATER contents" data-target="CopyButton" data-props="{&quot;value&quot;:&quot;utils/audio_utils.py&quot;,&quot;classNames&quot;:&quot;text-xs ml-2&quot;,&quot;title&quot;:&quot;Copy path&quot;}"><button class="relative text-xs ml-2 inline-flex cursor-pointer items-center text-sm focus:outline-none  mx-0.5   text-gray-600 " title="Copy path" type="button"><svg class="" xmlns="http://www.w3.org/2000/svg" aria-hidden="true" fill="currentColor" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 32 32"><path d="M28,10V28H10V10H28m0-2H10a2,2,0,0,0-2,2V28a2,2,0,0,0,2,2H28a2,2,0,0,0,2-2V10a2,2,0,0,0-2-2Z" transform="translate(0)"></path><path d="M4,18H2V4A2,2,0,0,1,4,2H18V4H4Z" transform="translate(0)"></path><rect fill="none" width="32" height="32"></rect></svg>
	
	</button></div></div></div>

	
	</header>
			<div class="SVELTE_HYDRATER contents" data-target="LastCommit" data-props="{&quot;commitLast&quot;:{&quot;date&quot;:&quot;2023-07-12T04:56:38.000Z&quot;,&quot;subject&quot;:&quot;add model&quot;,&quot;authors&quot;:[{&quot;user&quot;:&quot;seungheondoh&quot;}],&quot;commit&quot;:{&quot;id&quot;:&quot;e48ca55169147a98c5d72304fd8891caf939d1a9&quot;,&quot;parentIds&quot;:[&quot;7ccf3fdcbce26e7c947774c280968cbe5b110ea3&quot;]},&quot;title&quot;:&quot;add model&quot;},&quot;repo&quot;:{&quot;name&quot;:&quot;seungheondoh/LP-Music-Caps-demo&quot;,&quot;type&quot;:&quot;space&quot;}}"><div class="from-gray-100-to-white flex items-baseline rounded-t-lg border border-b-0 bg-gradient-to-t px-3 py-2 dark:border-gray-800">
			<div class="mr-4 flex flex-none items-center truncate">seungheondoh
				
			</div>
		<div class="mr-4 truncate font-mono text-sm text-gray-500 hover:prose-a:underline"><!-- HTML_TAG_START -->add model<!-- HTML_TAG_END --></div>
		<a class="rounded border bg-gray-50 px-1.5 text-sm hover:underline dark:border-gray-800 dark:bg-gray-900" href="/spaces/seungheondoh/LP-Music-Caps-demo/commit/e48ca55169147a98c5d72304fd8891caf939d1a9">e48ca55</a>
		
		<time class="ml-auto hidden flex-none truncate pl-2 text-gray-500 dark:text-gray-400 lg:block" datetime="2023-07-12T04:56:38" title="Wed, 12 Jul 2023 04:56:38 GMT">over 1 year ago</time></div></div>
			<div class="relative flex flex-wrap items-center border px-3 py-1.5 text-sm text-gray-800 dark:border-gray-800 dark:bg-gray-900 ">
				<a class="my-1 mr-4 flex items-center hover:underline " href="/spaces/seungheondoh/LP-Music-Caps-demo/raw/main/utils/audio_utils.py"><svg class="mr-1.5" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 32 32" style="transform: rotate(360deg);"><path d="M31 16l-7 7l-1.41-1.41L28.17 16l-5.58-5.59L24 9l7 7z" fill="currentColor"></path><path d="M1 16l7-7l1.41 1.41L3.83 16l5.58 5.59L8 23l-7-7z" fill="currentColor"></path><path d="M12.419 25.484L17.639 6l1.932.518L14.35 26z" fill="currentColor"></path></svg>
							raw
						</a><div class="SVELTE_HYDRATER contents" data-target="CopyButton" data-props="{&quot;value&quot;:&quot;https://huggingface.co/spaces/seungheondoh/LP-Music-Caps-demo/resolve/main/utils/audio_utils.py&quot;,&quot;style&quot;:&quot;blank&quot;,&quot;label&quot;:&quot;Copy download link&quot;,&quot;classNames&quot;:&quot;my-1 mr-4 flex items-center no-underline hover:underline&quot;}"><button class="relative my-1 mr-4 flex items-center no-underline hover:underline       " title="Copy download link" type="button"><svg class="" xmlns="http://www.w3.org/2000/svg" aria-hidden="true" fill="currentColor" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 32 32"><path d="M28,10V28H10V10H28m0-2H10a2,2,0,0,0-2,2V28a2,2,0,0,0,2,2H28a2,2,0,0,0,2-2V10a2,2,0,0,0-2-2Z" transform="translate(0)"></path><path d="M4,18H2V4A2,2,0,0,1,4,2H18V4H4Z" transform="translate(0)"></path><rect fill="none" width="32" height="32"></rect></svg>
	<span class="ml-1.5 ">Copy download link</span>
	</button></div><a class="my-1 mr-4 flex items-center hover:underline " href="/spaces/seungheondoh/LP-Music-Caps-demo/commits/main/utils/audio_utils.py"><svg class="mr-1.5" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 32 32" style="transform: rotate(360deg);"><path d="M16 4C9.383 4 4 9.383 4 16s5.383 12 12 12s12-5.383 12-12S22.617 4 16 4zm0 2c5.535 0 10 4.465 10 10s-4.465 10-10 10S6 21.535 6 16S10.465 6 16 6zm-1 2v9h7v-2h-5V8z" fill="currentColor"></path></svg>
							history
						</a><a class="my-1 mr-4 flex items-center hover:underline " href="/spaces/seungheondoh/LP-Music-Caps-demo/blame/main/utils/audio_utils.py"><svg class="mr-1.5" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 32 32" style="transform: rotate(360deg);"><path d="M16 2a14 14 0 1 0 14 14A14 14 0 0 0 16 2zm0 26a12 12 0 1 1 12-12a12 12 0 0 1-12 12z" fill="currentColor"></path><path d="M11.5 11a2.5 2.5 0 1 0 2.5 2.5a2.48 2.48 0 0 0-2.5-2.5z" fill="currentColor"></path><path d="M20.5 11a2.5 2.5 0 1 0 2.5 2.5a2.48 2.48 0 0 0-2.5-2.5z" fill="currentColor"></path></svg>
							blame
						</a><a class="my-1 mr-4 flex items-center hover:underline text-green-600 dark:text-gray-300" href="/spaces/seungheondoh/LP-Music-Caps-demo/edit/main/utils/audio_utils.py"><svg class="mr-1.5" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 32 32"><path d="M2 26h28v2H2z" fill="currentColor"></path><path d="M25.4 9c.8-.8.8-2 0-2.8l-3.6-3.6c-.8-.8-2-.8-2.8 0l-15 15V24h6.4l15-15zm-5-5L24 7.6l-3 3L17.4 7l3-3zM6 22v-3.6l10-10l3.6 3.6l-10 10H6z" fill="currentColor"></path></svg>
							contribute
						</a><a class="my-1 mr-4 flex items-center hover:underline " href="/spaces/seungheondoh/LP-Music-Caps-demo/delete/main/utils/audio_utils.py"><svg class="mr-1.5" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" focusable="false" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 32 32"><path d="M12 12h2v12h-2z" fill="currentColor"></path><path d="M18 12h2v12h-2z" fill="currentColor"></path><path d="M4 6v2h2v20a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V8h2V6zm4 22V8h16v20z" fill="currentColor"></path><path d="M12 2h8v2h-8z" fill="currentColor"></path></svg>
							delete
						</a>

				<div class="mr-4 flex items-center"><div class="SVELTE_HYDRATER contents" data-target="ScanStatusBadge" data-props="{&quot;classNames&quot;:&quot;mr-2&quot;,&quot;scanStatus&quot;:{&quot;status&quot;:&quot;safe&quot;,&quot;protectAiScan&quot;:{&quot;status&quot;:&quot;unscanned&quot;},&quot;avScan&quot;:{&quot;status&quot;:&quot;safe&quot;},&quot;pickleImportScan&quot;:{&quot;status&quot;:&quot;unscanned&quot;,&quot;pickleImports&quot;:[]}},&quot;repo&quot;:{&quot;_id&quot;:&quot;64abba9a9faad01fb47c1ce2&quot;,&quot;gitalyUid&quot;:&quot;180be15482943e7560d22530cb7223b26a94a5eb8bdf00f750fc62986db56d49&quot;,&quot;type&quot;:&quot;space&quot;,&quot;name&quot;:&quot;seungheondoh/LP-Music-Caps-demo&quot;,&quot;config&quot;:{&quot;private&quot;:false,&quot;gated&quot;:false,&quot;discussionsDisabled&quot;:false,&quot;duplicationDisabled&quot;:false,&quot;region&quot;:&quot;us&quot;,&quot;gitaly&quot;:{&quot;storage&quot;:&quot;default&quot;,&quot;repoUid&quot;:&quot;180be15482943e7560d22530cb7223b26a94a5eb8bdf00f750fc62986db56d49&quot;,&quot;region&quot;:&quot;us&quot;},&quot;lfs&quot;:{&quot;bucket&quot;:&quot;lfs.huggingface.co&quot;,&quot;prefix&quot;:&quot;repos/18/0b/180be15482943e7560d22530cb7223b26a94a5eb8bdf00f750fc62986db56d49&quot;},&quot;lastDiscussion&quot;:1,&quot;spaces&quot;:{&quot;hardware&quot;:&quot;cpu-basic&quot;,&quot;storage&quot;:null,&quot;replicas&quot;:1,&quot;gcTimeout&quot;:86400}},&quot;updatedAt&quot;:&quot;2023-07-10T08:27:11.322Z&quot;,&quot;authorId&quot;:&quot;637c3504c292c0fd3f37361f&quot;,&quot;creatorId&quot;:&quot;637c3504c292c0fd3f37361f&quot;},&quot;revision&quot;:&quot;main&quot;,&quot;filePath&quot;:&quot;utils/audio_utils.py&quot;,&quot;openByDefault&quot;:false}"><div class="sm:relative mr-2"><button class="flex h-[1.125rem] select-none items-center gap-0.5 rounded border pl-0.5 pr-0.5 text-xs leading-tight text-gray-400 hover:cursor-pointer text-gray-400 hover:border-gray-200 hover:bg-gray-50 hover:text-gray-500 dark:border-gray-800 dark:hover:bg-gray-800 dark:hover:text-gray-200 "><svg class="flex-none" width="1em" height="1em" viewBox="0 0 22 28" fill="none" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" clip-rule="evenodd" d="M15.3634 10.3639C15.8486 10.8491 15.8486 11.6357 15.3634 12.1209L10.9292 16.5551C10.6058 16.8785 10.0814 16.8785 9.7579 16.5551L7.03051 13.8277C6.54532 13.3425 6.54532 12.5558 7.03051 12.0707C7.51569 11.5855 8.30234 11.5855 8.78752 12.0707L9.7579 13.041C10.0814 13.3645 10.6058 13.3645 10.9292 13.041L13.6064 10.3639C14.0916 9.8787 14.8782 9.8787 15.3634 10.3639Z" fill="currentColor"></path><path fill-rule="evenodd" clip-rule="evenodd" d="M10.6666 27.12C4.93329 25.28 0 19.2267 0 12.7867V6.52001C0 5.40001 0.693334 4.41334 1.73333 4.01334L9.73333 1.01334C10.3333 0.786673 11 0.786673 11.6 1.02667L19.6 4.02667C20.1083 4.21658 20.5465 4.55701 20.8562 5.00252C21.1659 5.44803 21.3324 5.97742 21.3333 6.52001V12.7867C21.3333 19.24 16.4 25.28 10.6666 27.12Z" fill="currentColor" fill-opacity="0.22"></path><path d="M10.0845 1.94967L10.0867 1.94881C10.4587 1.8083 10.8666 1.81036 11.2286 1.95515L11.2387 1.95919L11.2489 1.963L19.2489 4.963L19.25 4.96342C19.5677 5.08211 19.8416 5.29488 20.0351 5.57333C20.2285 5.85151 20.3326 6.18203 20.3333 6.52082C20.3333 6.52113 20.3333 6.52144 20.3333 6.52176L20.3333 12.7867C20.3333 18.6535 15.8922 24.2319 10.6666 26.0652C5.44153 24.2316 1 18.6409 1 12.7867V6.52001C1 5.82357 1.42893 5.20343 2.08883 4.94803L10.0845 1.94967Z" stroke="currentColor" stroke-opacity="0.30" stroke-width="2"></path></svg>

			<span class="mr-0.5 max-sm:hidden">Safe</span></button>

	</div></div>
						</div>

				<div class="flex items-center gap-x-3 dark:text-gray-300 sm:ml-auto"><div class="SVELTE_HYDRATER contents" data-target="LineWrapButton" data-props="{&quot;classNames&quot;:&quot;text-xs&quot;,&quot;lineSelectorClass&quot;:&quot;blob-line&quot;}">

<button class="text-xs" type="button" title="Toggle Line Wrap"><svg class="opacity-50" width="1em" height="1em" viewBox="0 0 12 11" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M0.75 1.25H11.25M0.75 5H9C9.75 5 11.25 5.375 11.25 6.875C11.25 8.375 9.99975 8.75 9.375 8.75H6M6 8.75L7.5 7.25M6 8.75L7.5 10.25M0.75 8.75H3.75" stroke="currentColor" stroke-width="1.125" stroke-linecap="round" stroke-linejoin="round"></path></svg></button></div>
					7.79 kB</div></div>

			<div class="relative min-h-[100px] rounded-b-lg border border-t-0 leading-tight dark:border-gray-800 dark:bg-gray-925">
				<div class="py-3"><div class="SVELTE_HYDRATER contents" data-target="BlobContent" data-props="{&quot;lines&quot;:[&quot;STR_CLIP_ID = <span class=\&quot;hljs-string\&quot;>&amp;#x27;clip_id&amp;#x27;</span>&quot;,&quot;STR_AUDIO_SIGNAL = <span class=\&quot;hljs-string\&quot;>&amp;#x27;audio_signal&amp;#x27;</span>&quot;,&quot;STR_TARGET_VECTOR = <span class=\&quot;hljs-string\&quot;>&amp;#x27;target_vector&amp;#x27;</span>&quot;,&quot;&quot;,&quot;&quot;,&quot;STR_CH_FIRST = <span class=\&quot;hljs-string\&quot;>&amp;#x27;channels_first&amp;#x27;</span>&quot;,&quot;STR_CH_LAST = <span class=\&quot;hljs-string\&quot;>&amp;#x27;channels_last&amp;#x27;</span>&quot;,&quot;&quot;,&quot;<span class=\&quot;hljs-keyword\&quot;>import</span> io&quot;,&quot;<span class=\&quot;hljs-keyword\&quot;>import</span> os&quot;,&quot;<span class=\&quot;hljs-keyword\&quot;>import</span> tqdm&quot;,&quot;<span class=\&quot;hljs-keyword\&quot;>import</span> logging&quot;,&quot;<span class=\&quot;hljs-keyword\&quot;>import</span> subprocess&quot;,&quot;<span class=\&quot;hljs-keyword\&quot;>from</span> typing <span class=\&quot;hljs-keyword\&quot;>import</span> <span class=\&quot;hljs-type\&quot;>Tuple</span>&quot;,&quot;<span class=\&quot;hljs-keyword\&quot;>from</span> pathlib <span class=\&quot;hljs-keyword\&quot;>import</span> Path&quot;,&quot;&quot;,&quot;<span class=\&quot;hljs-comment\&quot;># import librosa</span>&quot;,&quot;<span class=\&quot;hljs-keyword\&quot;>import</span> numpy <span class=\&quot;hljs-keyword\&quot;>as</span> np&quot;,&quot;<span class=\&quot;hljs-keyword\&quot;>import</span> soundfile <span class=\&quot;hljs-keyword\&quot;>as</span> sf&quot;,&quot;&quot;,&quot;<span class=\&quot;hljs-keyword\&quot;>import</span> itertools&quot;,&quot;<span class=\&quot;hljs-keyword\&quot;>from</span> numpy.fft <span class=\&quot;hljs-keyword\&quot;>import</span> irfft&quot;,&quot;&quot;,&quot;<span class=\&quot;hljs-keyword\&quot;>def</span> <span class=\&quot;hljs-title function_\&quot;>_resample_load_ffmpeg</span>(<span class=\&quot;hljs-params\&quot;>path: <span class=\&quot;hljs-built_in\&quot;>str</span>, sample_rate: <span class=\&quot;hljs-built_in\&quot;>int</span>, downmix_to_mono: <span class=\&quot;hljs-built_in\&quot;>bool</span></span>) -&amp;gt; <span class=\&quot;hljs-type\&quot;>Tuple</span>[np.ndarray, <span class=\&quot;hljs-built_in\&quot;>int</span>]:&quot;,&quot;    <span class=\&quot;hljs-string\&quot;>&amp;quot;&amp;quot;&amp;quot;</span>&quot;,&quot;<span class=\&quot;hljs-string\&quot;>    Decoding, downmixing, and downsampling by librosa.</span>&quot;,&quot;<span class=\&quot;hljs-string\&quot;>    Returns a channel-first audio signal.</span>&quot;,&quot;<span class=\&quot;hljs-string\&quot;></span>&quot;,&quot;<span class=\&quot;hljs-string\&quot;>    Args:</span>&quot;,&quot;<span class=\&quot;hljs-string\&quot;>        path:</span>&quot;,&quot;<span class=\&quot;hljs-string\&quot;>        sample_rate:</span>&quot;,&quot;<span class=\&quot;hljs-string\&quot;>        downmix_to_mono:</span>&quot;,&quot;<span class=\&quot;hljs-string\&quot;></span>&quot;,&quot;<span class=\&quot;hljs-string\&quot;>    Returns:</span>&quot;,&quot;<span class=\&quot;hljs-string\&quot;>        (audio signal, sample rate)</span>&quot;,&quot;<span class=\&quot;hljs-string\&quot;>    &amp;quot;&amp;quot;&amp;quot;</span>&quot;,&quot;&quot;,&quot;    <span class=\&quot;hljs-keyword\&quot;>def</span> <span class=\&quot;hljs-title function_\&quot;>_decode_resample_by_ffmpeg</span>(<span class=\&quot;hljs-params\&quot;>filename, sr</span>):&quot;,&quot;        <span class=\&quot;hljs-string\&quot;>&amp;quot;&amp;quot;&amp;quot;decode, downmix, and resample audio file&amp;quot;&amp;quot;&amp;quot;</span>&quot;,&quot;        channel_cmd = <span class=\&quot;hljs-string\&quot;>&amp;#x27;-ac 1 &amp;#x27;</span> <span class=\&quot;hljs-keyword\&quot;>if</span> downmix_to_mono <span class=\&quot;hljs-keyword\&quot;>else</span> <span class=\&quot;hljs-string\&quot;>&amp;#x27;&amp;#x27;</span>  <span class=\&quot;hljs-comment\&quot;># downmixing option</span>&quot;,&quot;        resampling_cmd = <span class=\&quot;hljs-string\&quot;>f&amp;#x27;-ar <span class=\&quot;hljs-subst\&quot;>{<span class=\&quot;hljs-built_in\&quot;>str</span>(sr)}</span>&amp;#x27;</span> <span class=\&quot;hljs-keyword\&quot;>if</span> sr <span class=\&quot;hljs-keyword\&quot;>else</span> <span class=\&quot;hljs-string\&quot;>&amp;#x27;&amp;#x27;</span>  <span class=\&quot;hljs-comment\&quot;># downsampling option</span>&quot;,&quot;        cmd = <span class=\&quot;hljs-string\&quot;>f&amp;quot;ffmpeg -i \\&amp;quot;<span class=\&quot;hljs-subst\&quot;>{filename}</span>\\&amp;quot; <span class=\&quot;hljs-subst\&quot;>{channel_cmd}</span> <span class=\&quot;hljs-subst\&quot;>{resampling_cmd}</span> -f wav -&amp;quot;</span>&quot;,&quot;        p = subprocess.Popen(cmd, shell=<span class=\&quot;hljs-literal\&quot;>True</span>, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)&quot;,&quot;        out, err = p.communicate()&quot;,&quot;        <span class=\&quot;hljs-keyword\&quot;>return</span> out&quot;,&quot;&quot;,&quot;    src, sr = sf.read(io.BytesIO(_decode_resample_by_ffmpeg(path, sr=sample_rate)))&quot;,&quot;    <span class=\&quot;hljs-keyword\&quot;>return</span> src.T, sr&quot;,&quot;&quot;,&quot;&quot;,&quot;<span class=\&quot;hljs-keyword\&quot;>def</span> <span class=\&quot;hljs-title function_\&quot;>_resample_load_librosa</span>(<span class=\&quot;hljs-params\&quot;>path: <span class=\&quot;hljs-built_in\&quot;>str</span>, sample_rate: <span class=\&quot;hljs-built_in\&quot;>int</span>, downmix_to_mono: <span class=\&quot;hljs-built_in\&quot;>bool</span>, **kwargs</span>) -&amp;gt; <span class=\&quot;hljs-type\&quot;>Tuple</span>[np.ndarray, <span class=\&quot;hljs-built_in\&quot;>int</span>]:&quot;,&quot;    <span class=\&quot;hljs-string\&quot;>&amp;quot;&amp;quot;&amp;quot;</span>&quot;,&quot;<span class=\&quot;hljs-string\&quot;>    Decoding, downmixing, and downsampling by librosa.</span>&quot;,&quot;<span class=\&quot;hljs-string\&quot;>    Returns a channel-first audio signal.</span>&quot;,&quot;<span class=\&quot;hljs-string\&quot;>    &amp;quot;&amp;quot;&amp;quot;</span>&quot;,&quot;    src, sr = librosa.load(path, sr=sample_rate, mono=downmix_to_mono, **kwargs)&quot;,&quot;    <span class=\&quot;hljs-keyword\&quot;>return</span> src, sr&quot;,&quot;&quot;,&quot;&quot;,&quot;<span class=\&quot;hljs-keyword\&quot;>def</span> <span class=\&quot;hljs-title function_\&quot;>load_audio</span>(<span class=\&quot;hljs-params\&quot;></span>&quot;,&quot;<span class=\&quot;hljs-params\&quot;>    path: <span class=\&quot;hljs-built_in\&quot;>str</span> <span class=\&quot;hljs-keyword\&quot;>or</span> Path,</span>&quot;,&quot;<span class=\&quot;hljs-params\&quot;>    ch_format: <span class=\&quot;hljs-built_in\&quot;>str</span>,</span>&quot;,&quot;<span class=\&quot;hljs-params\&quot;>    sample_rate: <span class=\&quot;hljs-built_in\&quot;>int</span> = <span class=\&quot;hljs-literal\&quot;>None</span>,</span>&quot;,&quot;<span class=\&quot;hljs-params\&quot;>    downmix_to_mono: <span class=\&quot;hljs-built_in\&quot;>bool</span> = <span class=\&quot;hljs-literal\&quot;>False</span>,</span>&quot;,&quot;<span class=\&quot;hljs-params\&quot;>    resample_by: <span class=\&quot;hljs-built_in\&quot;>str</span> = <span class=\&quot;hljs-string\&quot;>&amp;#x27;ffmpeg&amp;#x27;</span>,</span>&quot;,&quot;<span class=\&quot;hljs-params\&quot;>    **kwargs,</span>&quot;,&quot;<span class=\&quot;hljs-params\&quot;></span>) -&amp;gt; <span class=\&quot;hljs-type\&quot;>Tuple</span>[np.ndarray, <span class=\&quot;hljs-built_in\&quot;>int</span>]:&quot;,&quot;    <span class=\&quot;hljs-string\&quot;>&amp;quot;&amp;quot;&amp;quot;A wrapper of librosa.load that:</span>&quot;,&quot;<span class=\&quot;hljs-string\&quot;>        - forces the returned audio to be 2-dim,</span>&quot;,&quot;<span class=\&quot;hljs-string\&quot;>        - defaults to sr=None, and</span>&quot;,&quot;<span class=\&quot;hljs-string\&quot;>        - defaults to downmix_to_mono=False.</span>&quot;,&quot;<span class=\&quot;hljs-string\&quot;></span>&quot;,&quot;<span class=\&quot;hljs-string\&quot;>    The audio decoding is done by `audioread` or `soundfile` package and ultimately, often by ffmpeg.</span>&quot;,&quot;<span class=\&quot;hljs-string\&quot;>    The resampling is done by `librosa`&amp;#x27;s child package `resampy`.</span>&quot;,&quot;<span class=\&quot;hljs-string\&quot;></span>&quot;,&quot;<span class=\&quot;hljs-string\&quot;>    Args:</span>&quot;,&quot;<span class=\&quot;hljs-string\&quot;>        path: audio file path</span>&quot;,&quot;<span class=\&quot;hljs-string\&quot;>        ch_format: one of &amp;#x27;channels_first&amp;#x27; or &amp;#x27;channels_last&amp;#x27;</span>&quot;,&quot;<span class=\&quot;hljs-string\&quot;>        sample_rate: target sampling rate. if None, use the rate of the audio file</span>&quot;,&quot;<span class=\&quot;hljs-string\&quot;>        downmix_to_mono:</span>&quot;,&quot;<span class=\&quot;hljs-string\&quot;>        resample_by (str): &amp;#x27;librosa&amp;#x27; or &amp;#x27;ffmpeg&amp;#x27;. it decides backend for audio decoding and resampling.</span>&quot;,&quot;<span class=\&quot;hljs-string\&quot;>        **kwargs: keyword args for librosa.load - offset, duration, dtype, res_type.</span>&quot;,&quot;<span class=\&quot;hljs-string\&quot;></span>&quot;,&quot;<span class=\&quot;hljs-string\&quot;>    Returns:</span>&quot;,&quot;<span class=\&quot;hljs-string\&quot;>        (audio, sr) tuple</span>&quot;,&quot;<span class=\&quot;hljs-string\&quot;>    &amp;quot;&amp;quot;&amp;quot;</span>&quot;,&quot;    <span class=\&quot;hljs-keyword\&quot;>if</span> ch_format <span class=\&quot;hljs-keyword\&quot;>not</span> <span class=\&quot;hljs-keyword\&quot;>in</span> (STR_CH_FIRST, STR_CH_LAST):&quot;,&quot;        <span class=\&quot;hljs-keyword\&quot;>raise</span> ValueError(<span class=\&quot;hljs-string\&quot;>f&amp;#x27;ch_format is wrong here -&amp;gt; <span class=\&quot;hljs-subst\&quot;>{ch_format}</span>&amp;#x27;</span>)&quot;,&quot;&quot;,&quot;    <span class=\&quot;hljs-keyword\&quot;>if</span> os.stat(path).st_size &amp;gt; <span class=\&quot;hljs-number\&quot;>8000</span>:&quot;,&quot;        <span class=\&quot;hljs-keyword\&quot;>if</span> resample_by == <span class=\&quot;hljs-string\&quot;>&amp;#x27;librosa&amp;#x27;</span>:&quot;,&quot;            src, sr = _resample_load_librosa(path, sample_rate, downmix_to_mono, **kwargs)&quot;,&quot;        <span class=\&quot;hljs-keyword\&quot;>elif</span> resample_by == <span class=\&quot;hljs-string\&quot;>&amp;#x27;ffmpeg&amp;#x27;</span>:&quot;,&quot;            src, sr = _resample_load_ffmpeg(path, sample_rate, downmix_to_mono)&quot;,&quot;        <span class=\&quot;hljs-keyword\&quot;>else</span>:&quot;,&quot;            <span class=\&quot;hljs-keyword\&quot;>raise</span> NotImplementedError(<span class=\&quot;hljs-string\&quot;>f&amp;#x27;resample_by: &amp;quot;<span class=\&quot;hljs-subst\&quot;>{resample_by}</span>&amp;quot; is not supposred yet&amp;#x27;</span>)&quot;,&quot;    <span class=\&quot;hljs-keyword\&quot;>else</span>:&quot;,&quot;        <span class=\&quot;hljs-keyword\&quot;>raise</span> ValueError(<span class=\&quot;hljs-string\&quot;>&amp;#x27;Given audio is too short!&amp;#x27;</span>)&quot;,&quot;    <span class=\&quot;hljs-keyword\&quot;>return</span> src, sr&quot;,&quot;&quot;,&quot;    <span class=\&quot;hljs-comment\&quot;># if src.ndim == 1:</span>&quot;,&quot;    <span class=\&quot;hljs-comment\&quot;>#     src = np.expand_dims(src, axis=0)</span>&quot;,&quot;    <span class=\&quot;hljs-comment\&quot;># # now always 2d and channels_first</span>&quot;,&quot;&quot;,&quot;    <span class=\&quot;hljs-comment\&quot;># if ch_format == STR_CH_FIRST:</span>&quot;,&quot;    <span class=\&quot;hljs-comment\&quot;>#     return src, sr</span>&quot;,&quot;    <span class=\&quot;hljs-comment\&quot;># else:</span>&quot;,&quot;    <span class=\&quot;hljs-comment\&quot;>#     return src.T, sr</span>&quot;,&quot;&quot;,&quot;<span class=\&quot;hljs-keyword\&quot;>def</span> <span class=\&quot;hljs-title function_\&quot;>ms</span>(<span class=\&quot;hljs-params\&quot;>x</span>):&quot;,&quot;    <span class=\&quot;hljs-string\&quot;>&amp;quot;&amp;quot;&amp;quot;Mean value of signal `x` squared.</span>&quot;,&quot;<span class=\&quot;hljs-string\&quot;>    :param x: Dynamic quantity.</span>&quot;,&quot;<span class=\&quot;hljs-string\&quot;>    :returns: Mean squared of `x`.</span>&quot;,&quot;<span class=\&quot;hljs-string\&quot;>    &amp;quot;&amp;quot;&amp;quot;</span>&quot;,&quot;    <span class=\&quot;hljs-keyword\&quot;>return</span> (np.<span class=\&quot;hljs-built_in\&quot;>abs</span>(x)**<span class=\&quot;hljs-number\&quot;>2.0</span>).mean()&quot;,&quot;&quot;,&quot;<span class=\&quot;hljs-keyword\&quot;>def</span> <span class=\&quot;hljs-title function_\&quot;>normalize</span>(<span class=\&quot;hljs-params\&quot;>y, x=<span class=\&quot;hljs-literal\&quot;>None</span></span>):&quot;,&quot;    <span class=\&quot;hljs-string\&quot;>&amp;quot;&amp;quot;&amp;quot;normalize power in y to a (standard normal) white noise signal.</span>&quot;,&quot;<span class=\&quot;hljs-string\&quot;>    Optionally normalize to power in signal `x`.</span>&quot;,&quot;<span class=\&quot;hljs-string\&quot;>    #The mean power of a Gaussian with :math:`\\\\mu=0` and :math:`\\\\sigma=1` is 1.</span>&quot;,&quot;<span class=\&quot;hljs-string\&quot;>    &amp;quot;&amp;quot;&amp;quot;</span>&quot;,&quot;    <span class=\&quot;hljs-keyword\&quot;>if</span> x <span class=\&quot;hljs-keyword\&quot;>is</span> <span class=\&quot;hljs-keyword\&quot;>not</span> <span class=\&quot;hljs-literal\&quot;>None</span>:&quot;,&quot;        x = ms(x)&quot;,&quot;    <span class=\&quot;hljs-keyword\&quot;>else</span>:&quot;,&quot;        x = <span class=\&quot;hljs-number\&quot;>1.0</span>&quot;,&quot;    <span class=\&quot;hljs-keyword\&quot;>return</span> y * np.sqrt(x / ms(y))&quot;,&quot;&quot;,&quot;<span class=\&quot;hljs-keyword\&quot;>def</span> <span class=\&quot;hljs-title function_\&quot;>noise</span>(<span class=\&quot;hljs-params\&quot;>N, color=<span class=\&quot;hljs-string\&quot;>&amp;#x27;white&amp;#x27;</span>, state=<span class=\&quot;hljs-literal\&quot;>None</span></span>):&quot;,&quot;    <span class=\&quot;hljs-string\&quot;>&amp;quot;&amp;quot;&amp;quot;Noise generator.</span>&quot;,&quot;<span class=\&quot;hljs-string\&quot;>    :param N: Amount of samples.</span>&quot;,&quot;<span class=\&quot;hljs-string\&quot;>    :param color: Color of noise.</span>&quot;,&quot;<span class=\&quot;hljs-string\&quot;>    :param state: State of PRNG.</span>&quot;,&quot;<span class=\&quot;hljs-string\&quot;>    :type state: :class:`np.random.RandomState`</span>&quot;,&quot;<span class=\&quot;hljs-string\&quot;>    &amp;quot;&amp;quot;&amp;quot;</span>&quot;,&quot;    <span class=\&quot;hljs-keyword\&quot;>try</span>:&quot;,&quot;        <span class=\&quot;hljs-keyword\&quot;>return</span> _noise_generators[color](N, state)&quot;,&quot;    <span class=\&quot;hljs-keyword\&quot;>except</span> KeyError:&quot;,&quot;        <span class=\&quot;hljs-keyword\&quot;>raise</span> ValueError(<span class=\&quot;hljs-string\&quot;>&amp;quot;Incorrect color.&amp;quot;</span>)&quot;,&quot;&quot;,&quot;<span class=\&quot;hljs-keyword\&quot;>def</span> <span class=\&quot;hljs-title function_\&quot;>white</span>(<span class=\&quot;hljs-params\&quot;>N, state=<span class=\&quot;hljs-literal\&quot;>None</span></span>):&quot;,&quot;    <span class=\&quot;hljs-string\&quot;>&amp;quot;&amp;quot;&amp;quot;</span>&quot;,&quot;<span class=\&quot;hljs-string\&quot;>    White noise.</span>&quot;,&quot;<span class=\&quot;hljs-string\&quot;>    :param N: Amount of samples.</span>&quot;,&quot;<span class=\&quot;hljs-string\&quot;>    :param state: State of PRNG.</span>&quot;,&quot;<span class=\&quot;hljs-string\&quot;>    :type state: :class:`np.random.RandomState`</span>&quot;,&quot;<span class=\&quot;hljs-string\&quot;>    White noise has a constant power density. It&amp;#x27;s narrowband spectrum is therefore flat.</span>&quot;,&quot;<span class=\&quot;hljs-string\&quot;>    The power in white noise will increase by a factor of two for each octave band,</span>&quot;,&quot;<span class=\&quot;hljs-string\&quot;>    and therefore increases with 3 dB per octave.</span>&quot;,&quot;<span class=\&quot;hljs-string\&quot;>    &amp;quot;&amp;quot;&amp;quot;</span>&quot;,&quot;    state = np.random.RandomState() <span class=\&quot;hljs-keyword\&quot;>if</span> state <span class=\&quot;hljs-keyword\&quot;>is</span> <span class=\&quot;hljs-literal\&quot;>None</span> <span class=\&quot;hljs-keyword\&quot;>else</span> state&quot;,&quot;    <span class=\&quot;hljs-keyword\&quot;>return</span> state.randn(N)&quot;,&quot;&quot;,&quot;<span class=\&quot;hljs-keyword\&quot;>def</span> <span class=\&quot;hljs-title function_\&quot;>pink</span>(<span class=\&quot;hljs-params\&quot;>N, state=<span class=\&quot;hljs-literal\&quot;>None</span></span>):&quot;,&quot;    <span class=\&quot;hljs-string\&quot;>&amp;quot;&amp;quot;&amp;quot;</span>&quot;,&quot;<span class=\&quot;hljs-string\&quot;>    Pink noise.</span>&quot;,&quot;<span class=\&quot;hljs-string\&quot;>    :param N: Amount of samples.</span>&quot;,&quot;<span class=\&quot;hljs-string\&quot;>    :param state: State of PRNG.</span>&quot;,&quot;<span class=\&quot;hljs-string\&quot;>    :type state: :class:`np.random.RandomState`</span>&quot;,&quot;<span class=\&quot;hljs-string\&quot;>    Pink noise has equal power in bands that are proportionally wide.</span>&quot;,&quot;<span class=\&quot;hljs-string\&quot;>    Power density decreases with 3 dB per octave.</span>&quot;,&quot;<span class=\&quot;hljs-string\&quot;>    &amp;quot;&amp;quot;&amp;quot;</span>&quot;,&quot;    state = np.random.RandomState() <span class=\&quot;hljs-keyword\&quot;>if</span> state <span class=\&quot;hljs-keyword\&quot;>is</span> <span class=\&quot;hljs-literal\&quot;>None</span> <span class=\&quot;hljs-keyword\&quot;>else</span> state&quot;,&quot;    uneven = N % <span class=\&quot;hljs-number\&quot;>2</span>&quot;,&quot;    X = state.randn(N // <span class=\&quot;hljs-number\&quot;>2</span> + <span class=\&quot;hljs-number\&quot;>1</span> + uneven) + <span class=\&quot;hljs-number\&quot;>1j</span> * state.randn(N // <span class=\&quot;hljs-number\&quot;>2</span> + <span class=\&quot;hljs-number\&quot;>1</span> + uneven)&quot;,&quot;    S = np.sqrt(np.arange(<span class=\&quot;hljs-built_in\&quot;>len</span>(X)) + <span class=\&quot;hljs-number\&quot;>1.</span>)  <span class=\&quot;hljs-comment\&quot;># +1 to avoid divide by zero</span>&quot;,&quot;    y = (irfft(X / S)).real&quot;,&quot;    <span class=\&quot;hljs-keyword\&quot;>if</span> uneven:&quot;,&quot;        y = y[:-<span class=\&quot;hljs-number\&quot;>1</span>]&quot;,&quot;    <span class=\&quot;hljs-keyword\&quot;>return</span> normalize(y)&quot;,&quot;&quot;,&quot;<span class=\&quot;hljs-keyword\&quot;>def</span> <span class=\&quot;hljs-title function_\&quot;>blue</span>(<span class=\&quot;hljs-params\&quot;>N, state=<span class=\&quot;hljs-literal\&quot;>None</span></span>):&quot;,&quot;    <span class=\&quot;hljs-string\&quot;>&amp;quot;&amp;quot;&amp;quot;</span>&quot;,&quot;<span class=\&quot;hljs-string\&quot;>    Blue noise.</span>&quot;,&quot;<span class=\&quot;hljs-string\&quot;>    :param N: Amount of samples.</span>&quot;,&quot;<span class=\&quot;hljs-string\&quot;>    :param state: State of PRNG.</span>&quot;,&quot;<span class=\&quot;hljs-string\&quot;>    :type state: :class:`np.random.RandomState`</span>&quot;,&quot;<span class=\&quot;hljs-string\&quot;>    Power increases with 6 dB per octave.</span>&quot;,&quot;<span class=\&quot;hljs-string\&quot;>    Power density increases with 3 dB per octave.</span>&quot;,&quot;<span class=\&quot;hljs-string\&quot;>    &amp;quot;&amp;quot;&amp;quot;</span>&quot;,&quot;    state = np.random.RandomState() <span class=\&quot;hljs-keyword\&quot;>if</span> state <span class=\&quot;hljs-keyword\&quot;>is</span> <span class=\&quot;hljs-literal\&quot;>None</span> <span class=\&quot;hljs-keyword\&quot;>else</span> state&quot;,&quot;    uneven = N % <span class=\&quot;hljs-number\&quot;>2</span>&quot;,&quot;    X = state.randn(N // <span class=\&quot;hljs-number\&quot;>2</span> + <span class=\&quot;hljs-number\&quot;>1</span> + uneven) + <span class=\&quot;hljs-number\&quot;>1j</span> * state.randn(N // <span class=\&quot;hljs-number\&quot;>2</span> + <span class=\&quot;hljs-number\&quot;>1</span> + uneven)&quot;,&quot;    S = np.sqrt(np.arange(<span class=\&quot;hljs-built_in\&quot;>len</span>(X)))  <span class=\&quot;hljs-comment\&quot;># Filter</span>&quot;,&quot;    y = (irfft(X * S)).real&quot;,&quot;    <span class=\&quot;hljs-keyword\&quot;>if</span> uneven:&quot;,&quot;        y = y[:-<span class=\&quot;hljs-number\&quot;>1</span>]&quot;,&quot;    <span class=\&quot;hljs-keyword\&quot;>return</span> normalize(y)&quot;,&quot;&quot;,&quot;<span class=\&quot;hljs-keyword\&quot;>def</span> <span class=\&quot;hljs-title function_\&quot;>brown</span>(<span class=\&quot;hljs-params\&quot;>N, state=<span class=\&quot;hljs-literal\&quot;>None</span></span>):&quot;,&quot;    <span class=\&quot;hljs-string\&quot;>&amp;quot;&amp;quot;&amp;quot;</span>&quot;,&quot;<span class=\&quot;hljs-string\&quot;>    Violet noise.</span>&quot;,&quot;<span class=\&quot;hljs-string\&quot;>    :param N: Amount of samples.</span>&quot;,&quot;<span class=\&quot;hljs-string\&quot;>    :param state: State of PRNG.</span>&quot;,&quot;<span class=\&quot;hljs-string\&quot;>    :type state: :class:`np.random.RandomState`</span>&quot;,&quot;<span class=\&quot;hljs-string\&quot;>    Power decreases with -3 dB per octave.</span>&quot;,&quot;<span class=\&quot;hljs-string\&quot;>    Power density decreases with 6 dB per octave.</span>&quot;,&quot;<span class=\&quot;hljs-string\&quot;>    &amp;quot;&amp;quot;&amp;quot;</span>&quot;,&quot;    state = np.random.RandomState() <span class=\&quot;hljs-keyword\&quot;>if</span> state <span class=\&quot;hljs-keyword\&quot;>is</span> <span class=\&quot;hljs-literal\&quot;>None</span> <span class=\&quot;hljs-keyword\&quot;>else</span> state&quot;,&quot;    uneven = N % <span class=\&quot;hljs-number\&quot;>2</span>&quot;,&quot;    X = state.randn(N // <span class=\&quot;hljs-number\&quot;>2</span> + <span class=\&quot;hljs-number\&quot;>1</span> + uneven) + <span class=\&quot;hljs-number\&quot;>1j</span> * state.randn(N // <span class=\&quot;hljs-number\&quot;>2</span> + <span class=\&quot;hljs-number\&quot;>1</span> + uneven)&quot;,&quot;    S = (np.arange(<span class=\&quot;hljs-built_in\&quot;>len</span>(X)) + <span class=\&quot;hljs-number\&quot;>1</span>)  <span class=\&quot;hljs-comment\&quot;># Filter</span>&quot;,&quot;    y = (irfft(X / S)).real&quot;,&quot;    <span class=\&quot;hljs-keyword\&quot;>if</span> uneven:&quot;,&quot;        y = y[:-<span class=\&quot;hljs-number\&quot;>1</span>]&quot;,&quot;    <span class=\&quot;hljs-keyword\&quot;>return</span> normalize(y)&quot;,&quot;&quot;,&quot;<span class=\&quot;hljs-keyword\&quot;>def</span> <span class=\&quot;hljs-title function_\&quot;>violet</span>(<span class=\&quot;hljs-params\&quot;>N, state=<span class=\&quot;hljs-literal\&quot;>None</span></span>):&quot;,&quot;    <span class=\&quot;hljs-string\&quot;>&amp;quot;&amp;quot;&amp;quot;</span>&quot;,&quot;<span class=\&quot;hljs-string\&quot;>    Violet noise. Power increases with 6 dB per octave.</span>&quot;,&quot;<span class=\&quot;hljs-string\&quot;>    :param N: Amount of samples.</span>&quot;,&quot;<span class=\&quot;hljs-string\&quot;>    :param state: State of PRNG.</span>&quot;,&quot;<span class=\&quot;hljs-string\&quot;>    :type state: :class:`np.random.RandomState`</span>&quot;,&quot;<span class=\&quot;hljs-string\&quot;>    Power increases with +9 dB per octave.</span>&quot;,&quot;<span class=\&quot;hljs-string\&quot;>    Power density increases with +6 dB per octave.</span>&quot;,&quot;<span class=\&quot;hljs-string\&quot;>    &amp;quot;&amp;quot;&amp;quot;</span>&quot;,&quot;    state = np.random.RandomState() <span class=\&quot;hljs-keyword\&quot;>if</span> state <span class=\&quot;hljs-keyword\&quot;>is</span> <span class=\&quot;hljs-literal\&quot;>None</span> <span class=\&quot;hljs-keyword\&quot;>else</span> state&quot;,&quot;    uneven = N % <span class=\&quot;hljs-number\&quot;>2</span>&quot;,&quot;    X = state.randn(N // <span class=\&quot;hljs-number\&quot;>2</span> + <span class=\&quot;hljs-number\&quot;>1</span> + uneven) + <span class=\&quot;hljs-number\&quot;>1j</span> * state.randn(N // <span class=\&quot;hljs-number\&quot;>2</span> + <span class=\&quot;hljs-number\&quot;>1</span> + uneven)&quot;,&quot;    S = (np.arange(<span class=\&quot;hljs-built_in\&quot;>len</span>(X)))  <span class=\&quot;hljs-comment\&quot;># Filter</span>&quot;,&quot;    y = (irfft(X * S)).real&quot;,&quot;    <span class=\&quot;hljs-keyword\&quot;>if</span> uneven:&quot;,&quot;        y = y[:-<span class=\&quot;hljs-number\&quot;>1</span>]&quot;,&quot;    <span class=\&quot;hljs-keyword\&quot;>return</span> normalize(y)&quot;,&quot;&quot;,&quot;_noise_generators = {&quot;,&quot;    <span class=\&quot;hljs-string\&quot;>&amp;#x27;white&amp;#x27;</span>: white,&quot;,&quot;    <span class=\&quot;hljs-string\&quot;>&amp;#x27;pink&amp;#x27;</span>: pink,&quot;,&quot;    <span class=\&quot;hljs-string\&quot;>&amp;#x27;blue&amp;#x27;</span>: blue,&quot;,&quot;    <span class=\&quot;hljs-string\&quot;>&amp;#x27;brown&amp;#x27;</span>: brown,&quot;,&quot;    <span class=\&quot;hljs-string\&quot;>&amp;#x27;violet&amp;#x27;</span>: violet,&quot;,&quot;}&quot;,&quot;&quot;,&quot;<span class=\&quot;hljs-keyword\&quot;>def</span> <span class=\&quot;hljs-title function_\&quot;>noise_generator</span>(<span class=\&quot;hljs-params\&quot;>N=<span class=\&quot;hljs-number\&quot;>44100</span>, color=<span class=\&quot;hljs-string\&quot;>&amp;#x27;white&amp;#x27;</span>, state=<span class=\&quot;hljs-literal\&quot;>None</span></span>):&quot;,&quot;    <span class=\&quot;hljs-string\&quot;>&amp;quot;&amp;quot;&amp;quot;Noise generator.</span>&quot;,&quot;<span class=\&quot;hljs-string\&quot;>    :param N: Amount of unique samples to generate.</span>&quot;,&quot;<span class=\&quot;hljs-string\&quot;>    :param color: Color of noise.</span>&quot;,&quot;<span class=\&quot;hljs-string\&quot;>    Generate `N` amount of unique samples and cycle over these samples.</span>&quot;,&quot;<span class=\&quot;hljs-string\&quot;>    &amp;quot;&amp;quot;&amp;quot;</span>&quot;,&quot;    <span class=\&quot;hljs-comment\&quot;>#yield from itertools.cycle(noise(N, color)) # Python 3.3</span>&quot;,&quot;    <span class=\&quot;hljs-keyword\&quot;>for</span> sample <span class=\&quot;hljs-keyword\&quot;>in</span> itertools.cycle(noise(N, color, state)):&quot;,&quot;        <span class=\&quot;hljs-keyword\&quot;>yield</span> sample&quot;,&quot;&quot;,&quot;<span class=\&quot;hljs-keyword\&quot;>def</span> <span class=\&quot;hljs-title function_\&quot;>heaviside</span>(<span class=\&quot;hljs-params\&quot;>N</span>):&quot;,&quot;    <span class=\&quot;hljs-string\&quot;>&amp;quot;&amp;quot;&amp;quot;Heaviside.</span>&quot;,&quot;<span class=\&quot;hljs-string\&quot;>    Returns the value 0 for `x &amp;lt; 0`, 1 for `x &amp;gt; 0`, and 1/2 for `x = 0`.</span>&quot;,&quot;<span class=\&quot;hljs-string\&quot;>    &amp;quot;&amp;quot;&amp;quot;</span>&quot;,&quot;    <span class=\&quot;hljs-keyword\&quot;>return</span> <span class=\&quot;hljs-number\&quot;>0.5</span> * (np.sign(N) + <span class=\&quot;hljs-number\&quot;>1</span>)&quot;],&quot;lineSelectorClass&quot;:&quot;blob-line&quot;,&quot;context&quot;:{&quot;repo&quot;:{&quot;name&quot;:&quot;seungheondoh/LP-Music-Caps-demo&quot;,&quot;type&quot;:&quot;space&quot;},&quot;revision&quot;:&quot;83027ae8b0806281fa539ebf43f69b016265bcee&quot;,&quot;path&quot;:&quot;utils/audio_utils.py&quot;}}">

<div class="relative text-sm"><div class="overflow-x-auto"><table class="min-w-full border-collapse font-mono"><tbody><tr class="" id="L1">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="1"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->STR_CLIP_ID = <span class="hljs-string">&#x27;clip_id&#x27;</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L2">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="2"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->STR_AUDIO_SIGNAL = <span class="hljs-string">&#x27;audio_signal&#x27;</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L3">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="3"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->STR_TARGET_VECTOR = <span class="hljs-string">&#x27;target_vector&#x27;</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L4">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="4"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->
<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L5">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="5"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->
<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L6">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="6"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->STR_CH_FIRST = <span class="hljs-string">&#x27;channels_first&#x27;</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L7">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="7"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->STR_CH_LAST = <span class="hljs-string">&#x27;channels_last&#x27;</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L8">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="8"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->
<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L9">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="9"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-keyword">import</span> io<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L10">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="10"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-keyword">import</span> os<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L11">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="11"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-keyword">import</span> tqdm<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L12">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="12"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-keyword">import</span> logging<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L13">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="13"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-keyword">import</span> subprocess<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L14">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="14"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-keyword">from</span> typing <span class="hljs-keyword">import</span> <span class="hljs-type">Tuple</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L15">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="15"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-keyword">from</span> pathlib <span class="hljs-keyword">import</span> Path<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L16">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="16"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->
<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L17">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="17"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-comment"># import librosa</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L18">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="18"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-keyword">import</span> numpy <span class="hljs-keyword">as</span> np<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L19">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="19"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-keyword">import</span> soundfile <span class="hljs-keyword">as</span> sf<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L20">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="20"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->
<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L21">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="21"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-keyword">import</span> itertools<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L22">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="22"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-keyword">from</span> numpy.fft <span class="hljs-keyword">import</span> irfft<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L23">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="23"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->
<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L24">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="24"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-keyword">def</span> <span class="hljs-title function_">_resample_load_ffmpeg</span>(<span class="hljs-params">path: <span class="hljs-built_in">str</span>, sample_rate: <span class="hljs-built_in">int</span>, downmix_to_mono: <span class="hljs-built_in">bool</span></span>) -&gt; <span class="hljs-type">Tuple</span>[np.ndarray, <span class="hljs-built_in">int</span>]:<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L25">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="25"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->    <span class="hljs-string">&quot;&quot;&quot;</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L26">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="26"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-string">    Decoding, downmixing, and downsampling by librosa.</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L27">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="27"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-string">    Returns a channel-first audio signal.</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L28">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="28"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-string"></span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L29">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="29"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-string">    Args:</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L30">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="30"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-string">        path:</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L31">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="31"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-string">        sample_rate:</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L32">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="32"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-string">        downmix_to_mono:</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L33">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="33"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-string"></span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L34">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="34"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-string">    Returns:</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L35">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="35"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-string">        (audio signal, sample rate)</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L36">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="36"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-string">    &quot;&quot;&quot;</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L37">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="37"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->
<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L38">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="38"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->    <span class="hljs-keyword">def</span> <span class="hljs-title function_">_decode_resample_by_ffmpeg</span>(<span class="hljs-params">filename, sr</span>):<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L39">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="39"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->        <span class="hljs-string">&quot;&quot;&quot;decode, downmix, and resample audio file&quot;&quot;&quot;</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L40">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="40"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->        channel_cmd = <span class="hljs-string">&#x27;-ac 1 &#x27;</span> <span class="hljs-keyword">if</span> downmix_to_mono <span class="hljs-keyword">else</span> <span class="hljs-string">&#x27;&#x27;</span>  <span class="hljs-comment"># downmixing option</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L41">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="41"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->        resampling_cmd = <span class="hljs-string">f&#x27;-ar <span class="hljs-subst">{<span class="hljs-built_in">str</span>(sr)}</span>&#x27;</span> <span class="hljs-keyword">if</span> sr <span class="hljs-keyword">else</span> <span class="hljs-string">&#x27;&#x27;</span>  <span class="hljs-comment"># downsampling option</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L42">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="42"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->        cmd = <span class="hljs-string">f&quot;ffmpeg -i \&quot;<span class="hljs-subst">{filename}</span>\&quot; <span class="hljs-subst">{channel_cmd}</span> <span class="hljs-subst">{resampling_cmd}</span> -f wav -&quot;</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L43">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="43"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->        p = subprocess.Popen(cmd, shell=<span class="hljs-literal">True</span>, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L44">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="44"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->        out, err = p.communicate()<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L45">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="45"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->        <span class="hljs-keyword">return</span> out<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L46">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="46"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->
<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L47">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="47"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->    src, sr = sf.read(io.BytesIO(_decode_resample_by_ffmpeg(path, sr=sample_rate)))<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L48">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="48"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->    <span class="hljs-keyword">return</span> src.T, sr<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L49">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="49"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->
<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L50">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="50"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->
<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L51">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="51"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-keyword">def</span> <span class="hljs-title function_">_resample_load_librosa</span>(<span class="hljs-params">path: <span class="hljs-built_in">str</span>, sample_rate: <span class="hljs-built_in">int</span>, downmix_to_mono: <span class="hljs-built_in">bool</span>, **kwargs</span>) -&gt; <span class="hljs-type">Tuple</span>[np.ndarray, <span class="hljs-built_in">int</span>]:<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L52">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="52"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->    <span class="hljs-string">&quot;&quot;&quot;</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L53">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="53"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-string">    Decoding, downmixing, and downsampling by librosa.</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L54">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="54"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-string">    Returns a channel-first audio signal.</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L55">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="55"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-string">    &quot;&quot;&quot;</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L56">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="56"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->    src, sr = librosa.load(path, sr=sample_rate, mono=downmix_to_mono, **kwargs)<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L57">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="57"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->    <span class="hljs-keyword">return</span> src, sr<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L58">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="58"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->
<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L59">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="59"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->
<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L60">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="60"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-keyword">def</span> <span class="hljs-title function_">load_audio</span>(<span class="hljs-params"></span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L61">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="61"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-params">    path: <span class="hljs-built_in">str</span> <span class="hljs-keyword">or</span> Path,</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L62">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="62"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-params">    ch_format: <span class="hljs-built_in">str</span>,</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L63">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="63"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-params">    sample_rate: <span class="hljs-built_in">int</span> = <span class="hljs-literal">None</span>,</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L64">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="64"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-params">    downmix_to_mono: <span class="hljs-built_in">bool</span> = <span class="hljs-literal">False</span>,</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L65">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="65"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-params">    resample_by: <span class="hljs-built_in">str</span> = <span class="hljs-string">&#x27;ffmpeg&#x27;</span>,</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L66">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="66"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-params">    **kwargs,</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L67">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="67"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-params"></span>) -&gt; <span class="hljs-type">Tuple</span>[np.ndarray, <span class="hljs-built_in">int</span>]:<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L68">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="68"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->    <span class="hljs-string">&quot;&quot;&quot;A wrapper of librosa.load that:</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L69">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="69"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-string">        - forces the returned audio to be 2-dim,</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L70">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="70"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-string">        - defaults to sr=None, and</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L71">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="71"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-string">        - defaults to downmix_to_mono=False.</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L72">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="72"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-string"></span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L73">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="73"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-string">    The audio decoding is done by `audioread` or `soundfile` package and ultimately, often by ffmpeg.</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L74">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="74"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-string">    The resampling is done by `librosa`&#x27;s child package `resampy`.</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L75">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="75"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-string"></span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L76">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="76"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-string">    Args:</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L77">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="77"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-string">        path: audio file path</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L78">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="78"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-string">        ch_format: one of &#x27;channels_first&#x27; or &#x27;channels_last&#x27;</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L79">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="79"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-string">        sample_rate: target sampling rate. if None, use the rate of the audio file</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L80">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="80"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-string">        downmix_to_mono:</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L81">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="81"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-string">        resample_by (str): &#x27;librosa&#x27; or &#x27;ffmpeg&#x27;. it decides backend for audio decoding and resampling.</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L82">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="82"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-string">        **kwargs: keyword args for librosa.load - offset, duration, dtype, res_type.</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L83">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="83"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-string"></span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L84">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="84"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-string">    Returns:</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L85">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="85"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-string">        (audio, sr) tuple</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L86">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="86"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-string">    &quot;&quot;&quot;</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L87">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="87"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->    <span class="hljs-keyword">if</span> ch_format <span class="hljs-keyword">not</span> <span class="hljs-keyword">in</span> (STR_CH_FIRST, STR_CH_LAST):<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L88">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="88"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->        <span class="hljs-keyword">raise</span> ValueError(<span class="hljs-string">f&#x27;ch_format is wrong here -&gt; <span class="hljs-subst">{ch_format}</span>&#x27;</span>)<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L89">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="89"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->
<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L90">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="90"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->    <span class="hljs-keyword">if</span> os.stat(path).st_size &gt; <span class="hljs-number">8000</span>:<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L91">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="91"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->        <span class="hljs-keyword">if</span> resample_by == <span class="hljs-string">&#x27;librosa&#x27;</span>:<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L92">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="92"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->            src, sr = _resample_load_librosa(path, sample_rate, downmix_to_mono, **kwargs)<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L93">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="93"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->        <span class="hljs-keyword">elif</span> resample_by == <span class="hljs-string">&#x27;ffmpeg&#x27;</span>:<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L94">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="94"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->            src, sr = _resample_load_ffmpeg(path, sample_rate, downmix_to_mono)<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L95">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="95"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->        <span class="hljs-keyword">else</span>:<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L96">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="96"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->            <span class="hljs-keyword">raise</span> NotImplementedError(<span class="hljs-string">f&#x27;resample_by: &quot;<span class="hljs-subst">{resample_by}</span>&quot; is not supposred yet&#x27;</span>)<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L97">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="97"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->    <span class="hljs-keyword">else</span>:<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L98">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="98"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->        <span class="hljs-keyword">raise</span> ValueError(<span class="hljs-string">&#x27;Given audio is too short!&#x27;</span>)<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L99">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="99"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->    <span class="hljs-keyword">return</span> src, sr<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L100">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="100"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->
<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L101">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="101"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->    <span class="hljs-comment"># if src.ndim == 1:</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L102">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="102"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->    <span class="hljs-comment">#     src = np.expand_dims(src, axis=0)</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L103">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="103"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->    <span class="hljs-comment"># # now always 2d and channels_first</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L104">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="104"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->
<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L105">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="105"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->    <span class="hljs-comment"># if ch_format == STR_CH_FIRST:</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L106">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="106"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->    <span class="hljs-comment">#     return src, sr</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L107">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="107"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->    <span class="hljs-comment"># else:</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L108">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="108"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->    <span class="hljs-comment">#     return src.T, sr</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L109">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="109"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->
<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L110">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="110"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-keyword">def</span> <span class="hljs-title function_">ms</span>(<span class="hljs-params">x</span>):<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L111">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="111"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->    <span class="hljs-string">&quot;&quot;&quot;Mean value of signal `x` squared.</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L112">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="112"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-string">    :param x: Dynamic quantity.</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L113">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="113"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-string">    :returns: Mean squared of `x`.</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L114">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="114"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-string">    &quot;&quot;&quot;</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L115">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="115"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->    <span class="hljs-keyword">return</span> (np.<span class="hljs-built_in">abs</span>(x)**<span class="hljs-number">2.0</span>).mean()<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L116">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="116"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->
<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L117">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="117"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-keyword">def</span> <span class="hljs-title function_">normalize</span>(<span class="hljs-params">y, x=<span class="hljs-literal">None</span></span>):<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L118">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="118"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->    <span class="hljs-string">&quot;&quot;&quot;normalize power in y to a (standard normal) white noise signal.</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L119">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="119"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-string">    Optionally normalize to power in signal `x`.</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L120">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="120"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-string">    #The mean power of a Gaussian with :math:`\\mu=0` and :math:`\\sigma=1` is 1.</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L121">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="121"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-string">    &quot;&quot;&quot;</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L122">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="122"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->    <span class="hljs-keyword">if</span> x <span class="hljs-keyword">is</span> <span class="hljs-keyword">not</span> <span class="hljs-literal">None</span>:<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L123">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="123"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->        x = ms(x)<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L124">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="124"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->    <span class="hljs-keyword">else</span>:<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L125">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="125"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->        x = <span class="hljs-number">1.0</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L126">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="126"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->    <span class="hljs-keyword">return</span> y * np.sqrt(x / ms(y))<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L127">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="127"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->
<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L128">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="128"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-keyword">def</span> <span class="hljs-title function_">noise</span>(<span class="hljs-params">N, color=<span class="hljs-string">&#x27;white&#x27;</span>, state=<span class="hljs-literal">None</span></span>):<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L129">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="129"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->    <span class="hljs-string">&quot;&quot;&quot;Noise generator.</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L130">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="130"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-string">    :param N: Amount of samples.</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L131">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="131"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-string">    :param color: Color of noise.</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L132">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="132"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-string">    :param state: State of PRNG.</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L133">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="133"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-string">    :type state: :class:`np.random.RandomState`</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L134">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="134"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-string">    &quot;&quot;&quot;</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L135">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="135"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->    <span class="hljs-keyword">try</span>:<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L136">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="136"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->        <span class="hljs-keyword">return</span> _noise_generators[color](N, state)<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L137">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="137"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->    <span class="hljs-keyword">except</span> KeyError:<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L138">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="138"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->        <span class="hljs-keyword">raise</span> ValueError(<span class="hljs-string">&quot;Incorrect color.&quot;</span>)<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L139">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="139"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->
<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L140">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="140"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-keyword">def</span> <span class="hljs-title function_">white</span>(<span class="hljs-params">N, state=<span class="hljs-literal">None</span></span>):<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L141">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="141"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->    <span class="hljs-string">&quot;&quot;&quot;</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L142">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="142"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-string">    White noise.</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L143">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="143"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-string">    :param N: Amount of samples.</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L144">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="144"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-string">    :param state: State of PRNG.</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L145">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="145"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-string">    :type state: :class:`np.random.RandomState`</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L146">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="146"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-string">    White noise has a constant power density. It&#x27;s narrowband spectrum is therefore flat.</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L147">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="147"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-string">    The power in white noise will increase by a factor of two for each octave band,</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L148">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="148"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-string">    and therefore increases with 3 dB per octave.</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L149">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="149"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-string">    &quot;&quot;&quot;</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L150">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="150"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->    state = np.random.RandomState() <span class="hljs-keyword">if</span> state <span class="hljs-keyword">is</span> <span class="hljs-literal">None</span> <span class="hljs-keyword">else</span> state<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L151">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="151"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->    <span class="hljs-keyword">return</span> state.randn(N)<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L152">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="152"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->
<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L153">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="153"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-keyword">def</span> <span class="hljs-title function_">pink</span>(<span class="hljs-params">N, state=<span class="hljs-literal">None</span></span>):<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L154">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="154"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->    <span class="hljs-string">&quot;&quot;&quot;</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L155">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="155"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-string">    Pink noise.</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L156">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="156"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-string">    :param N: Amount of samples.</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L157">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="157"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-string">    :param state: State of PRNG.</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L158">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="158"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-string">    :type state: :class:`np.random.RandomState`</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L159">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="159"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-string">    Pink noise has equal power in bands that are proportionally wide.</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L160">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="160"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-string">    Power density decreases with 3 dB per octave.</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L161">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="161"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-string">    &quot;&quot;&quot;</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L162">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="162"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->    state = np.random.RandomState() <span class="hljs-keyword">if</span> state <span class="hljs-keyword">is</span> <span class="hljs-literal">None</span> <span class="hljs-keyword">else</span> state<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L163">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="163"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->    uneven = N % <span class="hljs-number">2</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L164">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="164"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->    X = state.randn(N // <span class="hljs-number">2</span> + <span class="hljs-number">1</span> + uneven) + <span class="hljs-number">1j</span> * state.randn(N // <span class="hljs-number">2</span> + <span class="hljs-number">1</span> + uneven)<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L165">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="165"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->    S = np.sqrt(np.arange(<span class="hljs-built_in">len</span>(X)) + <span class="hljs-number">1.</span>)  <span class="hljs-comment"># +1 to avoid divide by zero</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L166">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="166"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->    y = (irfft(X / S)).real<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L167">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="167"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->    <span class="hljs-keyword">if</span> uneven:<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L168">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="168"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->        y = y[:-<span class="hljs-number">1</span>]<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L169">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="169"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->    <span class="hljs-keyword">return</span> normalize(y)<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L170">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="170"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->
<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L171">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="171"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-keyword">def</span> <span class="hljs-title function_">blue</span>(<span class="hljs-params">N, state=<span class="hljs-literal">None</span></span>):<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L172">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="172"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->    <span class="hljs-string">&quot;&quot;&quot;</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L173">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="173"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-string">    Blue noise.</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L174">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="174"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-string">    :param N: Amount of samples.</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L175">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="175"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-string">    :param state: State of PRNG.</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L176">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="176"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-string">    :type state: :class:`np.random.RandomState`</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L177">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="177"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-string">    Power increases with 6 dB per octave.</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L178">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="178"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-string">    Power density increases with 3 dB per octave.</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L179">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="179"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-string">    &quot;&quot;&quot;</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L180">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="180"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->    state = np.random.RandomState() <span class="hljs-keyword">if</span> state <span class="hljs-keyword">is</span> <span class="hljs-literal">None</span> <span class="hljs-keyword">else</span> state<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L181">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="181"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->    uneven = N % <span class="hljs-number">2</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L182">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="182"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->    X = state.randn(N // <span class="hljs-number">2</span> + <span class="hljs-number">1</span> + uneven) + <span class="hljs-number">1j</span> * state.randn(N // <span class="hljs-number">2</span> + <span class="hljs-number">1</span> + uneven)<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L183">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="183"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->    S = np.sqrt(np.arange(<span class="hljs-built_in">len</span>(X)))  <span class="hljs-comment"># Filter</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L184">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="184"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->    y = (irfft(X * S)).real<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L185">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="185"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->    <span class="hljs-keyword">if</span> uneven:<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L186">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="186"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->        y = y[:-<span class="hljs-number">1</span>]<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L187">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="187"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->    <span class="hljs-keyword">return</span> normalize(y)<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L188">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="188"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->
<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L189">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="189"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-keyword">def</span> <span class="hljs-title function_">brown</span>(<span class="hljs-params">N, state=<span class="hljs-literal">None</span></span>):<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L190">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="190"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->    <span class="hljs-string">&quot;&quot;&quot;</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L191">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="191"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-string">    Violet noise.</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L192">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="192"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-string">    :param N: Amount of samples.</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L193">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="193"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-string">    :param state: State of PRNG.</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L194">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="194"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-string">    :type state: :class:`np.random.RandomState`</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L195">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="195"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-string">    Power decreases with -3 dB per octave.</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L196">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="196"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-string">    Power density decreases with 6 dB per octave.</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L197">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="197"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-string">    &quot;&quot;&quot;</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L198">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="198"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->    state = np.random.RandomState() <span class="hljs-keyword">if</span> state <span class="hljs-keyword">is</span> <span class="hljs-literal">None</span> <span class="hljs-keyword">else</span> state<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L199">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="199"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->    uneven = N % <span class="hljs-number">2</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L200">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="200"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->    X = state.randn(N // <span class="hljs-number">2</span> + <span class="hljs-number">1</span> + uneven) + <span class="hljs-number">1j</span> * state.randn(N // <span class="hljs-number">2</span> + <span class="hljs-number">1</span> + uneven)<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L201">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="201"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->    S = (np.arange(<span class="hljs-built_in">len</span>(X)) + <span class="hljs-number">1</span>)  <span class="hljs-comment"># Filter</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L202">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="202"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->    y = (irfft(X / S)).real<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L203">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="203"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->    <span class="hljs-keyword">if</span> uneven:<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L204">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="204"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->        y = y[:-<span class="hljs-number">1</span>]<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L205">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="205"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->    <span class="hljs-keyword">return</span> normalize(y)<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L206">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="206"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->
<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L207">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="207"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-keyword">def</span> <span class="hljs-title function_">violet</span>(<span class="hljs-params">N, state=<span class="hljs-literal">None</span></span>):<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L208">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="208"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->    <span class="hljs-string">&quot;&quot;&quot;</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L209">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="209"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-string">    Violet noise. Power increases with 6 dB per octave.</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L210">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="210"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-string">    :param N: Amount of samples.</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L211">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="211"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-string">    :param state: State of PRNG.</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L212">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="212"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-string">    :type state: :class:`np.random.RandomState`</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L213">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="213"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-string">    Power increases with +9 dB per octave.</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L214">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="214"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-string">    Power density increases with +6 dB per octave.</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L215">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="215"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-string">    &quot;&quot;&quot;</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L216">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="216"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->    state = np.random.RandomState() <span class="hljs-keyword">if</span> state <span class="hljs-keyword">is</span> <span class="hljs-literal">None</span> <span class="hljs-keyword">else</span> state<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L217">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="217"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->    uneven = N % <span class="hljs-number">2</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L218">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="218"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->    X = state.randn(N // <span class="hljs-number">2</span> + <span class="hljs-number">1</span> + uneven) + <span class="hljs-number">1j</span> * state.randn(N // <span class="hljs-number">2</span> + <span class="hljs-number">1</span> + uneven)<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L219">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="219"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->    S = (np.arange(<span class="hljs-built_in">len</span>(X)))  <span class="hljs-comment"># Filter</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L220">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="220"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->    y = (irfft(X * S)).real<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L221">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="221"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->    <span class="hljs-keyword">if</span> uneven:<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L222">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="222"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->        y = y[:-<span class="hljs-number">1</span>]<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L223">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="223"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->    <span class="hljs-keyword">return</span> normalize(y)<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L224">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="224"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->
<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L225">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="225"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->_noise_generators = {<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L226">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="226"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->    <span class="hljs-string">&#x27;white&#x27;</span>: white,<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L227">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="227"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->    <span class="hljs-string">&#x27;pink&#x27;</span>: pink,<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L228">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="228"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->    <span class="hljs-string">&#x27;blue&#x27;</span>: blue,<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L229">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="229"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->    <span class="hljs-string">&#x27;brown&#x27;</span>: brown,<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L230">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="230"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->    <span class="hljs-string">&#x27;violet&#x27;</span>: violet,<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L231">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="231"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->}<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L232">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="232"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->
<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L233">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="233"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-keyword">def</span> <span class="hljs-title function_">noise_generator</span>(<span class="hljs-params">N=<span class="hljs-number">44100</span>, color=<span class="hljs-string">&#x27;white&#x27;</span>, state=<span class="hljs-literal">None</span></span>):<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L234">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="234"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->    <span class="hljs-string">&quot;&quot;&quot;Noise generator.</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L235">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="235"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-string">    :param N: Amount of unique samples to generate.</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L236">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="236"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-string">    :param color: Color of noise.</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L237">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="237"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-string">    Generate `N` amount of unique samples and cycle over these samples.</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L238">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="238"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-string">    &quot;&quot;&quot;</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L239">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="239"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->    <span class="hljs-comment">#yield from itertools.cycle(noise(N, color)) # Python 3.3</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L240">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="240"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->    <span class="hljs-keyword">for</span> sample <span class="hljs-keyword">in</span> itertools.cycle(noise(N, color, state)):<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L241">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="241"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->        <span class="hljs-keyword">yield</span> sample<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L242">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="242"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->
<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L243">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="243"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-keyword">def</span> <span class="hljs-title function_">heaviside</span>(<span class="hljs-params">N</span>):<!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L244">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="244"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->    <span class="hljs-string">&quot;&quot;&quot;Heaviside.</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L245">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="245"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-string">    Returns the value 0 for `x &lt; 0`, 1 for `x &gt; 0`, and 1/2 for `x = 0`.</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L246">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="246"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START --><span class="hljs-string">    &quot;&quot;&quot;</span><!-- HTML_TAG_END --></td>
					</tr><tr class="" id="L247">
						
						<td class="blob-line-num w-1 cursor-pointer select-none pl-5 pr-3 text-right align-top text-gray-300 hover:text-black dark:hover:text-white" data-line-num="247"></td>
						<td class="blob-line overflow-visible whitespace-pre px-3"><!-- HTML_TAG_START -->    <span class="hljs-keyword">return</span> <span class="hljs-number">0.5</span> * (np.sign(N) + <span class="hljs-number">1</span>)<!-- HTML_TAG_END --></td>
					</tr></tbody></table></div>
	</div></div></div></div></section></div></main>

	</div>

		<script>
			import("\/front\/build\/kube-0f9fcea\/index.js");
			window.moonSha = "kube-0f9fcea\/";
			window.__hf_deferred = {};
		</script>

		<!-- Stripe -->
		<script>
			if (["hf.co", "huggingface.co"].includes(window.location.hostname)) {
				const script = document.createElement("script");
				script.src = "https://js.stripe.com/v3/";
				script.async = true;
				document.head.appendChild(script);
			}
		</script>
	</body>
</html>
