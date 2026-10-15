### Hola 👋, Soy **Sebastián Colombini**

Senior Software Engineer (10+ años de experiencia). Hoy construyo servicios **AWS serverless** (**Lambda, API Gateway, SQS, SNS, Step Functions, DynamoDB**) que reemplazan, dominio por dominio, el core de un monolito PHP legacy en producción. Vengo de plataformas de e-commerce de alto tráfico (**Magento / Adobe Commerce, WordPress**), y me interesa todo lo que tiene que seguir funcionando cuando un paso falla: colas, idempotencia y compensación.

Buscando roles de **backend y platform en e-commerce**.

---

### 🎯 Skills

```yaml
stack:
  cloud: [AWS, Lambda, API Gateway, SQS, SNS, Step Functions, DynamoDB, CloudWatch, X-Ray]
  backend: [Node.js (NestJS, Express), PHP (Laravel, Magento 2, WordPress), Python (Django)]
  apis: [REST, GraphQL (cliente y servidor), integraciones entre sistemas]
  calidad: [Jest, PHPUnit (mocks del SDK de AWS), CI/CD (GitHub Actions), Docker, Git]
  data: [PostgreSQL, MySQL, DynamoDB, Redis, MongoDB]
```

---

### ☁️ AWS serverless

| Proyecto | Stack | Concepto |
|----------|-------|----------|
| **[Serverless Order Pipeline](https://github.com/colombinis/serverless-order-pipeline)** | AWS (Lambda, API Gateway, SQS, Step Functions, DynamoDB, SNS) + Node.js 18 | Pipeline de fulfillment de órdenes: creación idempotente → reserva de inventario con escritura condicional → cobro → confirmación → notificación. Con DLQ, reintentos con backoff, compensación (saga) y observabilidad (logs estructurados, métricas, X-Ray, alarmas). |

---

### 🔩 Infraestructura y plataformas

| Proyecto | Stack | Concepto |
|----------|-------|----------|
| Shopify Theme Personalizado | Shopify + Liquid | Sections dinámicas, metafields y personalización avanzada |
| Django REST API | Django + DRF | API RESTful con JWT, paginación y documentación Swagger |
| Odoo ERP | Odoo (Community) | Módulos de inventario, ventas, contabilidad y manufactura |

---

### 🧠 Proyectos IA + PHP

| Proyecto | Stack | Concepto |
|----------|-------|----------|
| **[AI Product Descriptions (WooCommerce)](https://github.com/colombinis/ai-product-descriptions-woocommerce)** | WordPress + WooCommerce + OpenAI/Ollama + Docker | Plugin que genera descripciones de producto con IA, segmentadas por buyer persona (tono, audiencia, extensión). Soporte dual provider. |
| **[PHP + Ollama RAG Chatbot](https://github.com/colombinis/php-ollama-rag-chatbot)** | PHP vanilla + Ollama (llama3.2) + SQLite | Chatbot RAG completo: embeddings + búsqueda semántica + LLM local. Zero framework dependencies. Mock mode sin Ollama. |
| **[AI Admin Assistant (WordPress)](https://github.com/colombinis/ai-admin-assistant-wordpress)** | WordPress + RAG + Ollama + Docker | Chatbot RAG para el admin de WP: embeddings + búsqueda semántica + LLM local (llama3.2). Sin APIs externas, sin costos recurrentes. Mock mode sin GPU. |

### 🔧 Proyectos en desarrollo

| Proyecto | Stack | Concepto |
|----------|-------|----------|
| AI Automatizar carga de producto | Magento 2 / WooCommerce + LLM + Vision API | Módulo que genera descripciones de producto por perfil demográfico usando IA |
| AI Contenido ultra personalizado | WordPress + LLM client-side + GEO IP API | Plugin que genera contenido dinámico por segmentos de potenciales clientes |
| AI Admin Assistant (Magento 2) | Magento 2 + RAG + LLM local | Módulo que responde preguntas de configuración y soporte desde el admin de Magento 2 |
| n8n + PHP Workflows | n8n + Laravel APIs | Automatizaciones enterprise conectando CRMs, ERPs y e-commerce |
| Magento 2 Hyva Theme | Magento 2 + Hyva + Alpine.js + Tailwind | Theme custom optimizado (LCP < 2.5s, zero JS bloqueante) |
| WordPress Headless + Astro | WordPress (API) + Astro.js | WP como CMS headless con frontend estático y preview en vivo |

---

### 🏢 Empresas donde trabajé

- **Fenicio.io** — Backend Developer (AWS serverless: Lambda, SQS, API Gateway; migración de un monolito PHP)
- **Ameba** — Senior Software Engineer (performance, CI/CD, integraciones con Django)
- **Valtech** — Senior Software Engineer (Magento 2: estabilización post-migración, soporte L2/L3)
- **Making Sense LLC** — Senior PHP Developer (WordPress, Laravel, Shopify, AWS)
- **TradeHelm, Inc.** — Senior Software Engineer (Laravel, Vue.js, React, GraphQL)
- **Globant** — Senior Software Engineer (Drupal, PHP)
- *Y anteriormente: SoftING SRL, EIyS S.A. — desde 2002*

---

### 📫 Contacto

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=flat&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/sebastian-colombini/) [![X](https://img.shields.io/badge/X-000000?style=flat&logo=x&logoColor=white)](https://x.com/seba_colombini) [![Web](https://img.shields.io/badge/Web-sacsi.com.ar-2ea44f?style=flat)](https://www.sacsi.com.ar)
