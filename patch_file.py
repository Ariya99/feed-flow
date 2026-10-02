import re

with open("shared/src/commonMain/kotlin/com/prof18/feedflow/shared/domain/feed/FeedFetcherRepository.kt", "r") as f:
    content = f.read()

# Add import
if "import kotlinx.coroutines.flow.mapNotNull" not in content:
    content = content.replace("import kotlin.time.Clock\n", "import kotlin.time.Clock\nimport kotlinx.coroutines.flow.mapNotNull\n")

# Move asFlow
content = content.replace(
"""        feedSourceUrls
            .mapNotNull { feedSource ->""",
"""        feedSourceUrls
            .asFlow()
            .mapNotNull { feedSource ->""")

content = content.replace(
"""                }
            }
            .asFlow()
            .flatMapMerge""",
"""                }
            }
            .flatMapMerge""")

with open("shared/src/commonMain/kotlin/com/prof18/feedflow/shared/domain/feed/FeedFetcherRepository.kt", "w") as f:
    f.write(content)
