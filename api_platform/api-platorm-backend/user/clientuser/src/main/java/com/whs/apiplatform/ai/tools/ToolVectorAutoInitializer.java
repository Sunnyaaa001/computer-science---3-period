//package com.whs.apiplatform.ai.tools;
//
//import dev.langchain4j.agent.tool.Tool;
//import dev.langchain4j.data.document.Metadata;
//import dev.langchain4j.data.segment.TextSegment;
//
//import dev.langchain4j.model.ollama.OllamaEmbeddingModel;
//import dev.langchain4j.store.embedding.EmbeddingStore;
//import lombok.RequiredArgsConstructor;
//import org.springframework.boot.CommandLineRunner;
//import org.springframework.context.ApplicationContext;
//import org.springframework.stereotype.Component;
//
//import java.lang.reflect.Method;
//
//@Component
//@RequiredArgsConstructor
//public class ToolVectorAutoInitializer implements CommandLineRunner {
//
//    private final EmbeddingStore<TextSegment> embeddingStore;
//    private final OllamaEmbeddingModel ollamaEmbeddingModel;
//    private final ApplicationContext applicationContext;
//
//    @Override
//    public void run(String... args) throws Exception {
//        String[] beanNames = applicationContext.getBeanDefinitionNames();
//        for (String beanName : beanNames) {
//            Object bean = applicationContext.getBean(beanName);
//            Method[] methods = bean.getClass().getDeclaredMethods();
//            for (Method method : methods) {
//                if (method.isAnnotationPresent(Tool.class)){
//                    Tool tool = method.getAnnotation(Tool.class);
//                    String[] values = tool.value();
//                    String toolDescription = (values.length > 0 && !values[0].isEmpty())
//                            ? values[0]
//                            : method.getName();
//                    TextSegment textSegment = TextSegment.from(toolDescription, Metadata.from("methodName", method.getName()));
//                    embeddingStore.add(ollamaEmbeddingModel.embed(textSegment).content(),textSegment);
//                }
//            }
//        }
//    }
//}
