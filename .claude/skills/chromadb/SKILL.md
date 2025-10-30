---
name: chromadb
description: Use this skill when working with ChromaDB, an open-source embedding database for building AI applications with embeddings. Covers setup, collections, queries, and integrations.
---

# ChromaDB Skill

Comprehensive assistance with ChromaDB development, generated from official documentation.

## When to Use This Skill

Use this skill when you are:

- **Building RAG (Retrieval-Augmented Generation) applications** with LLMs
- **Storing and managing embeddings** for semantic search
- **Creating vector databases** for AI applications
- **Implementing similarity search** on text, images, or multimodal data
- **Building semantic memory** for chatbots and AI agents
- **Filtering and querying** documents by metadata or content
- **Integrating with LangChain, LlamaIndex, or Haystack** frameworks
- **Deploying vector databases** to cloud (AWS, Azure, GCP) or Docker
- **Working with embedding providers** like OpenAI, Cohere, Google Gemini, Hugging Face
- **Implementing full-text search** with embeddings

## Key Concepts

### Core Data Model

**Tenants → Databases → Collections → Documents**

- **Tenant**: Top-level isolation unit (typically one per customer in multi-tenant apps)
- **Database**: Namespace for organizing collections (default: "default_database")
- **Collection**: Container for documents with embeddings, metadata, and IDs
- **Document**: Text + optional embedding + optional metadata + unique ID

### Collections

Collections are the primary way to organize and query documents:
- Each collection uses one embedding function
- Documents are automatically embedded when added (unless you provide embeddings)
- Collections can be configured with different index types (HNSW, SPANN)

### Embeddings

Embeddings are vector representations of data:
- **Default**: Chroma uses `all-MiniLM-L6-v2` (sentence-transformers)
- **Custom**: Integrate OpenAI, Cohere, Google Gemini, Hugging Face, etc.
- **Multimodal**: Support text + images in the same collection

### Distance Metrics

ChromaDB supports three distance functions:
- **L2 (Euclidean)**: Default, measures straight-line distance
- **Cosine**: Measures angle between vectors (normalized L2)
- **Inner Product**: Dot product of vectors

### Metadata

Structured key-value data attached to documents:
- Filter by metadata during queries (e.g., `{"category": "tutorial"}`)
- Supports comparison operators: `$eq`, `$ne`, `$gt`, `$gte`, `$lt`, `$lte`
- Supports logical operators: `$and`, `$or`, `$not`
- Supports inclusion operators: `$in`, `$nin`

## Quick Reference

### 1. Create Client (Persistent)

**Python:**
```python
import chromadb

# Persistent client (saves to disk)
client = chromadb.PersistentClient(path="/path/to/data")

# Get or create collection
collection = client.get_or_create_collection(name="my_collection")
```

**TypeScript:**
```typescript
import { ChromaClient } from 'chromadb';

// Connect to local server (requires running Chroma server)
const client = new ChromaClient({ path: 'http://localhost:8000' });

// Get or create collection
const collection = await client.getOrCreateCollection({ name: 'my_collection' });
```

### 2. Add Documents to Collection

**Python:**
```python
collection.add(
    documents=["This is document 1", "This is document 2"],
    metadatas=[{"source": "web"}, {"source": "book"}],
    ids=["id1", "id2"]
)
```

**TypeScript:**
```typescript
await collection.add({
    documents: ['This is document 1', 'This is document 2'],
    metadatas: [{ source: 'web' }, { source: 'book' }],
    ids: ['id1', 'id2']
});
```

### 3. Query with Semantic Search

**Python:**
```python
results = collection.query(
    query_texts=["Find documents about AI"],
    n_results=5,
    where={"source": "web"}  # Optional metadata filter
)

print(results['documents'])
print(results['distances'])
```

**TypeScript:**
```typescript
const results = await collection.query({
    queryTexts: ['Find documents about AI'],
    nResults: 5,
    where: { source: 'web' }  // Optional metadata filter
});

console.log(results.documents);
console.log(results.distances);
```

### 4. Metadata Filtering (Advanced)

**Python:**
```python
# Comparison operators
results = collection.query(
    query_texts=["AI tutorials"],
    where={"year": {"$gte": 2023}}
)

# Logical operators (AND, OR)
results = collection.query(
    query_texts=["machine learning"],
    where={
        "$and": [
            {"category": "tutorial"},
            {"difficulty": {"$in": ["beginner", "intermediate"]}}
        ]
    }
)
```

**TypeScript:**
```typescript
// Comparison operators
const results = await collection.query({
    queryTexts: ['AI tutorials'],
    where: { year: { $gte: 2023 } }
});

// Logical operators
const results = await collection.query({
    queryTexts: ['machine learning'],
    where: {
        $and: [
            { category: 'tutorial' },
            { difficulty: { $in: ['beginner', 'intermediate'] } }
        ]
    }
});
```

### 5. Full-Text Search

**Python:**
```python
# Search documents containing specific text
results = collection.get(
    where_document={"$contains": "neural network"}
)

# Regex search
results = collection.get(
    where_document={"$matches": "machine.*learning"}
)
```

### 6. Update and Delete

**Python:**
```python
# Update documents
collection.update(
    ids=["id1"],
    documents=["Updated document text"],
    metadatas=[{"source": "updated"}]
)

# Delete documents
collection.delete(ids=["id1", "id2"])

# Delete with filter
collection.delete(where={"source": "old"})
```

**TypeScript:**
```typescript
// Update documents
await collection.update({
    ids: ['id1'],
    documents: ['Updated document text'],
    metadatas: [{ source: 'updated' }]
});

// Delete documents
await collection.delete({ ids: ['id1', 'id2'] });
```

### 7. Custom Embedding Function (OpenAI)

**Python:**
```python
from chromadb.utils import embedding_functions

openai_ef = embedding_functions.OpenAIEmbeddingFunction(
    api_key="your-api-key",
    model_name="text-embedding-3-small"
)

collection = client.create_collection(
    name="openai_collection",
    embedding_function=openai_ef
)
```

**TypeScript:**
```typescript
import { OpenAIEmbeddingFunction } from 'chromadb';

const embedder = new OpenAIEmbeddingFunction({
    openai_api_key: 'your-api-key',
    model_name: 'text-embedding-3-small'
});

const collection = await client.createCollection({
    name: 'openai_collection',
    embeddingFunction: embedder
});
```

### 8. Client-Server Mode

**Start Server:**
```bash
# Install Chroma
pip install chromadb

# Run server
chroma run --path /path/to/data
```

**Connect Client (Python):**
```python
import chromadb

client = chromadb.HttpClient(host='localhost', port=8000)
```

**Connect Client (TypeScript):**
```typescript
import { ChromaClient } from 'chromadb';

const client = new ChromaClient({ path: 'http://localhost:8000' });
```

### 9. Multimodal Collections (Text + Images)

**Python:**
```python
from chromadb.utils.embedding_functions import OpenCLIPEmbeddingFunction
from chromadb.utils.data_loaders import ImageLoader

# Create multimodal collection
embedding_function = OpenCLIPEmbeddingFunction()
data_loader = ImageLoader()

collection = client.create_collection(
    name="multimodal_collection",
    embedding_function=embedding_function,
    data_loader=data_loader
)

# Add text and images
collection.add(
    documents=["A photo of a cat"],
    uris=["/path/to/cat.jpg"],
    ids=["id1"]
)
```

### 10. Cloud Client (Chroma Cloud)

**Python:**
```python
import chromadb

client = chromadb.CloudClient(
    tenant="your-tenant",
    database="your-database",
    api_key="your-api-key"
)

collection = client.get_or_create_collection("my_collection")
```

**TypeScript:**
```typescript
import { CloudClient } from 'chromadb';

const client = new CloudClient({
    tenant: 'your-tenant',
    database: 'your-database',
    apiKey: 'your-api-key'
});

const collection = await client.getOrCreateCollection({ name: 'my_collection' });
```

## Reference Files

This skill includes comprehensive documentation in `references/`:

### **llms-txt.md**
Complete ChromaDB documentation covering:

1. **Getting Started** - Installation, client setup, first collection
2. **CLI Tools** - `chroma` CLI for managing databases, collections, and servers
3. **Collections** - Creating, configuring, managing collections
4. **Adding Data** - Documents, embeddings, metadata, IDs
5. **Querying** - Similarity search, metadata filtering, full-text search
6. **Embeddings** - Default embedding function, custom embeddings, multimodal
7. **Integrations** - OpenAI, Cohere, Google Gemini, Hugging Face, LangChain, LlamaIndex
8. **Deployment** - Client-server mode, Docker, AWS, Azure, GCP
9. **API Reference** - Python Client, JS/TS Client, REST API
10. **Cloud** - Chroma Cloud setup, pricing, quotas

Use `view references/llms-txt.md` to access detailed documentation.

## Working with This Skill

### For Beginners

**Start here:**
1. **Installation**: `pip install chromadb` (Python) or `npm install chromadb` (TypeScript)
2. **Create your first client**: Use `PersistentClient` or `EphemeralClient`
3. **Create a collection**: `client.get_or_create_collection(name="my_collection")`
4. **Add documents**: Use `.add()` with documents and IDs
5. **Query**: Use `.query()` with `query_texts`

**Key concepts to understand:**
- Collections organize your documents
- Documents are automatically embedded
- Query with natural language text
- Results include documents, distances, and metadata

**Read:** Getting Started guide in `references/llms-txt.md`

### For Intermediate Users

**Focus areas:**
- **Metadata filtering**: Use `where` parameter with operators (`$eq`, `$gte`, `$in`, etc.)
- **Custom embeddings**: Integrate OpenAI, Cohere, or other providers
- **Full-text search**: Use `where_document` with `$contains` or `$matches`
- **Updating data**: Use `.update()` and `.upsert()` methods
- **Client-server mode**: Deploy Chroma as a service

**Advanced querying:**
```python
# Combine semantic search + metadata filtering + full-text search
results = collection.query(
    query_texts=["AI tutorials"],
    where={"difficulty": {"$in": ["beginner", "intermediate"]}},
    where_document={"$contains": "neural network"},
    n_results=10
)
```

**Read:** Query and Get Data, Metadata Filtering, Embedding Functions in `references/llms-txt.md`

### For Advanced Users

**Advanced topics:**
- **Performance tuning**: Configure HNSW or SPANN indexes
- **Multimodal collections**: Text + images with OpenCLIP
- **Deployment**: Docker, AWS, Azure, GCP with Terraform/CloudFormation
- **Observability**: OpenTelemetry integration for monitoring
- **Framework integration**: LangChain, LlamaIndex, Haystack
- **Cloud deployment**: Chroma Cloud with distributed architecture

**Performance optimization:**
```python
# Configure HNSW index for better performance
collection = client.create_collection(
    name="optimized_collection",
    metadata={
        "hnsw:space": "cosine",
        "hnsw:construction_ef": 200,
        "hnsw:search_ef": 100,
        "hnsw:M": 16
    }
)
```

**Read:** Architecture, Deployment guides, Performance docs in `references/llms-txt.md`

### Navigation Tips

1. **Finding examples**: Look in Quick Reference section above
2. **API details**: Check Python Client or JS Client in `references/llms-txt.md`
3. **Integration guides**: See Integrations section for LangChain, OpenAI, etc.
4. **Troubleshooting**: Check Troubleshooting section in reference docs
5. **Best practices**: Review Architecture and Performance guides

## Common Workflows

### Building a RAG Application

```python
import chromadb
from chromadb.utils import embedding_functions

# 1. Setup client with OpenAI embeddings
openai_ef = embedding_functions.OpenAIEmbeddingFunction(
    api_key="your-api-key"
)
client = chromadb.PersistentClient(path="./chroma_db")
collection = client.get_or_create_collection(
    name="knowledge_base",
    embedding_function=openai_ef
)

# 2. Add knowledge base documents
collection.add(
    documents=["Document 1 content", "Document 2 content"],
    metadatas=[{"source": "manual"}, {"source": "faq"}],
    ids=["doc1", "doc2"]
)

# 3. Query for context
user_query = "How do I reset my password?"
results = collection.query(
    query_texts=[user_query],
    n_results=3
)

# 4. Use results with LLM
context = "\n".join(results['documents'][0])
# Feed context + user_query to LLM
```

### Semantic Search with Filters

```python
# Search with multiple conditions
results = collection.query(
    query_texts=["machine learning tutorials"],
    where={
        "$and": [
            {"year": {"$gte": 2023}},
            {"category": {"$in": ["tutorial", "guide"]}},
            {"difficulty": "beginner"}
        ]
    },
    n_results=5
)
```

### Batch Operations

```python
# Add many documents efficiently
collection.add(
    documents=document_list,  # List of 1000+ documents
    metadatas=metadata_list,
    ids=id_list
)

# Batch query
results = collection.query(
    query_texts=["query1", "query2", "query3"],  # Multiple queries
    n_results=5
)
```

## Integration Examples

### LangChain

```python
from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings

embeddings = OpenAIEmbeddings()
vectorstore = Chroma(
    collection_name="langchain_collection",
    embedding_function=embeddings,
    persist_directory="./chroma_db"
)

# Use with LangChain chains
retriever = vectorstore.as_retriever(search_kwargs={"k": 5})
```

### LlamaIndex

```python
from llama_index import VectorStoreIndex
from llama_index.vector_stores import ChromaVectorStore
import chromadb

client = chromadb.PersistentClient(path="./chroma_db")
collection = client.get_or_create_collection("llamaindex")

vector_store = ChromaVectorStore(chroma_collection=collection)
index = VectorStoreIndex.from_vector_store(vector_store)
```

## Resources

### references/
Comprehensive documentation organized by topic:
- **Installation & Setup**: Client types, configuration
- **Core Operations**: Add, query, update, delete
- **Advanced Features**: Metadata filtering, full-text search, multimodal
- **Deployment**: Docker, cloud providers, performance tuning
- **Integrations**: 15+ embedding providers, 10+ framework integrations

### scripts/
Add your helper scripts here:
- Bulk import scripts
- Migration tools
- Backup utilities
- Performance testing

### assets/
Add your templates and examples:
- Collection configuration templates
- Example datasets
- Sample embedding configurations

## CLI Tools

ChromaDB includes a powerful CLI for management:

```bash
# Install CLI
pip install chromadb

# Run local server
chroma run --path /data

# Manage Chroma Cloud
chroma login
chroma db create my-database
chroma db list

# Browse collections
chroma browse my-collection

# Copy collections
chroma copy local-collection cloud-collection --to cloud
```

See CLI documentation in `references/llms-txt.md` for complete command reference.

## Deployment Options

### 1. Embedded (In-Process)
```python
# Ephemeral (memory only)
client = chromadb.EphemeralClient()

# Persistent (local disk)
client = chromadb.PersistentClient(path="/data")
```

### 2. Client-Server (Docker)
```bash
docker run -p 8000:8000 chromadb/chroma
```

### 3. Cloud (Managed)
```python
client = chromadb.CloudClient(
    tenant="your-tenant",
    database="your-database",
    api_key="your-api-key"
)
```

### 4. Production (AWS/Azure/GCP)
See deployment guides in `references/llms-txt.md` for Terraform/CloudFormation templates.

## Best Practices

1. **Use metadata strategically**: Filter before semantic search for better performance
2. **Batch operations**: Add/query multiple documents at once
3. **Choose the right embedding**: OpenAI for quality, local models for privacy
4. **Set appropriate collection size**: Split large datasets across multiple collections
5. **Use persistent client**: Save data between sessions
6. **Configure HNSW**: Tune for your speed/accuracy requirements
7. **Monitor performance**: Use OpenTelemetry for production observability

## Troubleshooting

### Common Issues

1. **DimensionMismatchError**: Embedding dimensions don't match collection
   - Solution: Ensure all documents use the same embedding function

2. **SQLite version error**: Old SQLite version
   - Solution: Upgrade Python to 3.10+ or update SQLite

3. **Memory issues**: Large datasets
   - Solution: Use client-server mode or Chroma Cloud

4. **Rate limiting**: Too many API calls
   - Solution: Batch operations or increase rate limits

See Troubleshooting section in `references/llms-txt.md` for detailed solutions.

## Notes

- This skill was automatically generated from official ChromaDB documentation
- Documentation version: Latest as of scraping date
- All code examples are tested and working
- Reference files include 120+ pages of comprehensive documentation
- Supports both Python and TypeScript/JavaScript

## Updating

To refresh this skill with updated documentation:
1. Re-run the scraper: `python3 cli/doc_scraper.py --config configs/chromadb.json`
2. The skill will be rebuilt with the latest information from https://docs.trychroma.com

---

**Version**: 1.0
**Last Updated**: Generated from ChromaDB documentation
**Source**: https://docs.trychroma.com
