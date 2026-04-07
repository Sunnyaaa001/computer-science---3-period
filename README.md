# computer-science---3-period
## Python Assignment
### Week 1 
For this week, in computer science parts, Tip calculator is that user can fill the price of meal and fill the discount percentages; And user can get the discounted price. In Smart Café Helper, users can order food and drinks whatever they want. Users can know how many calories that food has. In vanity plates, users can check whether car plates are valid. These assignments are based on Python. 
### Week 2
For this week, Computer Science has survival simulator assignment. This assignment should be based on numpy to generate menu list. Users can choose one to execute different functions. 
### Week 3
Computer Science: For this week, it focuses on python unit test. People need to learn how to write python unit tests code to test functions that people write.
### Week 4
In Computer Science, People should finish the presentation of solo project and feedback of project peer. 
### Week 5
In computer science, people should understand how to Pillow python library to modify pictures.
### Week 6
In Computer Science, people should understand some searching idea, like Depth-first search, Breath first search, greedy best-first search and A* search. In this assignment,
People should use MinMax idea to mock AI computing abilities to get current chess position. 
### Week 7
 In computer science, the assignment is minesweeper. Minesweeper involves several important ideas from AI and problem-solving. At its core, it is a Constraint Satisfaction Problem, where each revealed number acts as a constraint indicating how many mines exist in neighboring cells, and the player must find a configuration that satisfies all these constraints. The game also relies heavily on logical inference, since players deduce safe cells and mine locations by combining multiple constraints. In more complex situations where logic alone is insufficient, probabilistic reasoning is used to estimate the likelihood of a cell containing a mine and choose the safest option. Additionally, solving the game can involve search and backtracking, where different possible mine placements are explored and checked for consistency. Together, these ideas make Minesweeper a blend of deterministic reasoning and decision-making under uncertainty.

## Personal project: API Platform
### project structure

```
computer-science---3-period
├─ api_platform
│  ├─ api-platorm-backend
│  │  ├─ admin
│  │  │  ├─ app.py
│  │  │  ├─ config
│  │  │  │  └─ app_config.py
│  │  │  ├─ controller
│  │  │  │  ├─ api_category_controller.py
│  │  │  │  ├─ api_info_controller.py
│  │  │  │  └─ user_controller.py
│  │  │  ├─ model
│  │  │  │  ├─ api_category.py
│  │  │  │  ├─ api_info.py
│  │  │  │  └─ user.py
│  │  │  ├─ pyproject.toml
│  │  │  ├─ request
│  │  │  │  ├─ api_category_request.py
│  │  │  │  ├─ api_info_request.py
│  │  │  │  └─ user_request.py
│  │  │  ├─ resource
│  │  │  │  └─ application.yml
│  │  │  ├─ response
│  │  │  │  ├─ api_category_response.py
│  │  │  │  └─ api_info_response.py
│  │  │  └─ service
│  │  │     ├─ api_category_service.py
│  │  │     ├─ api_info_service.py
│  │  │     └─ user_service.py
│  │  ├─ common
│  │  │  ├─ config
│  │  │  │  └─ application_config.py
│  │  │  ├─ config_read
│  │  │  │  └─ config_read.py
│  │  │  ├─ db
│  │  │  │  ├─ base_model.py
│  │  │  │  └─ session.py
│  │  │  ├─ docerator
│  │  │  │  └─ docerator.py
│  │  │  ├─ exception
│  │  │  │  ├─ base
│  │  │  │  │  └─ base_exception.py
│  │  │  │  ├─ error
│  │  │  │  │  └─ error_code.py
│  │  │  │  └─ handler
│  │  │  │     └─ exception_handler.py
│  │  │  ├─ filter
│  │  │  │  └─ api_filter.py
│  │  │  ├─ id_generator
│  │  │  │  └─ id_util.py
│  │  │  ├─ jwt
│  │  │  │  └─ jwt_utils.py
│  │  │  ├─ password
│  │  │  │  └─ security.py
│  │  │  ├─ redis_util
│  │  │  │  └─ redis_util.py
│  │  │  ├─ response
│  │  │  │  └─ response_body.py
│  │  │  ├─ router
│  │  │  │  └─ router.py
│  │  │  ├─ schedule
│  │  │  │  ├─ controller
│  │  │  │  │  ├─ schedule_api.py
│  │  │  │  │  └─ schedule_log_api.py
│  │  │  │  ├─ enum
│  │  │  │  │  └─ task_enum.py
│  │  │  │  ├─ listener
│  │  │  │  │  └─ task_listener.py
│  │  │  │  ├─ model
│  │  │  │  │  └─ task_info.py
│  │  │  │  ├─ request_body
│  │  │  │  │  └─ request_param.py
│  │  │  │  ├─ response_body
│  │  │  │  │  └─ task_response.py
│  │  │  │  ├─ scheduler
│  │  │  │  │  └─ ap_scheduler.py
│  │  │  │  └─ service
│  │  │  │     ├─ schedule_log_service.py
│  │  │  │     └─ schedule_service.py
│  │  │  └─ user
│  │  │     └─ user_utils.py
│  │  ├─ poetry.lock
│  │  ├─ pyproject.toml
│  │  └─ user
│  │     ├─ clientuser
│  │     │  ├─ pom.xml
│  │     │  └─ src
│  │     │     └─ main
│  │     │        ├─ java
│  │     │        │  └─ com
│  │     │        │     └─ whs
│  │     │        │        └─ apiplatform
│  │     │        │           ├─ ai
│  │     │        │           │  ├─ controller
│  │     │        │           │  │  └─ AIAgentController.java
│  │     │        │           │  ├─ domain
│  │     │        │           │  │  ├─ AIChattingHistory.java
│  │     │        │           │  │  └─ AITopics.java
│  │     │        │           │  ├─ enums
│  │     │        │           │  │  └─ AIRouterEnum.java
│  │     │        │           │  ├─ mapper
│  │     │        │           │  │  ├─ AIChattingHistoryMapper.java
│  │     │        │           │  │  └─ AITopicMapper.java
│  │     │        │           │  ├─ request
│  │     │        │           │  │  └─ AIUserInputMessage.java
│  │     │        │           │  ├─ router
│  │     │        │           │  │  └─ AIAgentRouter.java
│  │     │        │           │  ├─ service
│  │     │        │           │  │  ├─ AIChattingHistoryServiceImpl.java
│  │     │        │           │  │  ├─ IAIAgentService.java
│  │     │        │           │  │  └─ IntentClassifier.java
│  │     │        │           │  └─ tools
│  │     │        │           │     ├─ AIConfig.java
│  │     │        │           │     ├─ AiConfigProperties.java
│  │     │        │           │     ├─ APITool.java
│  │     │        │           │     └─ ToolVectorAutoInitializer.java
│  │     │        │           ├─ api
│  │     │        │           │  ├─ controller
│  │     │        │           │  │  └─ APIInfoController.java
│  │     │        │           │  ├─ domain
│  │     │        │           │  │  ├─ APICategory.java
│  │     │        │           │  │  ├─ APIInfo.java
│  │     │        │           │  │  ├─ APIParamInfo.java
│  │     │        │           │  │  ├─ APIPluginInfo.java
│  │     │        │           │  │  ├─ APIResponseExample.java
│  │     │        │           │  │  └─ APIResponsePropertyInfo.java
│  │     │        │           │  ├─ mapper
│  │     │        │           │  │  ├─ ApiCategoryMapper.java
│  │     │        │           │  │  └─ APIInfoMapper.java
│  │     │        │           │  ├─ request
│  │     │        │           │  │  ├─ APIAIRequestParam.java
│  │     │        │           │  │  ├─ APIRequestParam.java
│  │     │        │           │  │  └─ CategoryParam.java
│  │     │        │           │  ├─ response
│  │     │        │           │  │  ├─ ApiCategoryResponse.java
│  │     │        │           │  │  ├─ ApiInfoResponse.java
│  │     │        │           │  │  ├─ ApiParamResponse.java
│  │     │        │           │  │  ├─ ApiPluginResponse.java
│  │     │        │           │  │  ├─ ApiResponseExamplesResponse.java
│  │     │        │           │  │  └─ ApiResponsePropertyResponse.java
│  │     │        │           │  └─ service
│  │     │        │           │     ├─ IAPICategoryService.java
│  │     │        │           │     ├─ IAPIInfoService.java
│  │     │        │           │     └─ impl
│  │     │        │           │        ├─ APICategoryServiceImpl.java
│  │     │        │           │        └─ APIInfoServiceImpl.java
│  │     │        │           ├─ platformApplication.java
│  │     │        │           └─ user
│  │     │        │              ├─ controller
│  │     │        │              │  └─ UserInfoController.java
│  │     │        │              ├─ domain
│  │     │        │              │  └─ UserInfo.java
│  │     │        │              ├─ mapper
│  │     │        │              │  └─ UserMapper.java
│  │     │        │              ├─ request
│  │     │        │              │  ├─ LoginUser.java
│  │     │        │              │  └─ RegisterUser.java
│  │     │        │              ├─ response
│  │     │        │              └─ service
│  │     │        │                 ├─ impl
│  │     │        │                 │  └─ UserServiceImpl.java
│  │     │        │                 └─ IUserService.java
│  │     │        └─ resources
│  │     │           ├─ application.yml
│  │     │           └─ mapper
│  │     │              ├─ ai
│  │     │              │  ├─ AIChattingHistoryMapper.xml
│  │     │              │  └─ AITopicMapper.xml
│  │     │              ├─ api
│  │     │              │  ├─ APICategoryMapper.xml
│  │     │              │  └─ ApiInfoMapper.xml
│  │     │              └─ user
│  │     │                 └─ UserMapper.xml
│  │     ├─ common
│  │     │  ├─ pom.xml
│  │     │  └─ src
│  │     │     └─ main
│  │     │        └─ java
│  │     │           └─ com
│  │     │              └─ whs
│  │     │                 └─ apiplatform
│  │     │                    └─ common
│  │     │                       ├─ exceptions
│  │     │                       │  ├─ BusinessException.java
│  │     │                       │  └─ GlobalExceptionHandler.java
│  │     │                       ├─ filter
│  │     │                       │  ├─ ApiFilter.java
│  │     │                       │  ├─ JwtAuthenticationEntryPoint.java
│  │     │                       │  └─ SecurityConfig.java
│  │     │                       ├─ http
│  │     │                       │  └─ HttpUtil.java
│  │     │                       ├─ id
│  │     │                       │  └─ SnowflakeIdUtil.java
│  │     │                       ├─ jackson
│  │     │                       │  └─ JacksonConfig.java
│  │     │                       ├─ model
│  │     │                       │  └─ BaseModel.java
│  │     │                       ├─ redis
│  │     │                       │  ├─ RedisConfig.java
│  │     │                       │  └─ RedisUtil.java
│  │     │                       ├─ response
│  │     │                       │  └─ ResponseResult.java
│  │     │                       ├─ thread
│  │     │                       │  └─ ThreadConfig.java
│  │     │                       ├─ token
│  │     │                       │  └─ TokenUtil.java
│  │     │                       ├─ tree
│  │     │                       │  ├─ TreeNode.java
│  │     │                       │  └─ TreeUtil.java
│  │     │                       └─ userinfo
│  │     │                          └─ UserInfoUtil.java
│  │     └─ pom.xml
│  └─ frontend
│     ├─ admin
│     │  └─ api-platform-admin-fronted
│     │     ├─ env.d.ts
│     │     ├─ index.html
│     │     ├─ package-lock.json
│     │     ├─ package.json
│     │     ├─ public
│     │     │  ├─ favicon.ico
│     │     │  └─ resources
│     │     │     └─ icon.png
│     │     ├─ README.md
│     │     ├─ src
│     │     │  ├─ App.vue
│     │     │  ├─ assets
│     │     │  │  ├─ css
│     │     │  │  │  └─ login.css
│     │     │  │  └─ resources
│     │     │  │     └─ login-bg.jpg
│     │     │  ├─ components
│     │     │  │  └─ auth.ts
│     │     │  ├─ main.ts
│     │     │  ├─ pages
│     │     │  │  ├─ api
│     │     │  │  │  └─ api.vue
│     │     │  │  ├─ categories
│     │     │  │  │  └─ categories.vue
│     │     │  │  ├─ home
│     │     │  │  │  └─ home.vue
│     │     │  │  ├─ index
│     │     │  │  │  └─ index.vue
│     │     │  │  └─ login
│     │     │  │     └─ login.vue
│     │     │  ├─ router
│     │     │  │  └─ router.ts
│     │     │  ├─ service
│     │     │  │  ├─ index.ts
│     │     │  │  └─ login.ts
│     │     │  └─ types
│     │     │     └─ basicresponse.ts
│     │     ├─ tsconfig.app.json
│     │     ├─ tsconfig.json
│     │     ├─ tsconfig.node.json
│     │     └─ vite.config.ts
│     └─ user
└─ README.md

```
### Admin Application
User can login this admin appliaction to register some APIs.
### Client Application 
User can login client user application to request these APIs
