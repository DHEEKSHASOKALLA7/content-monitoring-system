from .models import Keyword, ContentItem, Flag


def calculate_score(keyword, content):
    keyword_lower = keyword.lower()
    title = content.title.lower()
    body = content.body.lower()

    if keyword_lower in title:
        if keyword_lower == title:
            return 100
        return 70
    elif keyword_lower in body:
        return 40
    return 0


def run_scan():
    contents = ContentItem.objects.all()
    keywords = Keyword.objects.all()

    for content in contents:
        for keyword in keywords:
            score = calculate_score(keyword.name, content)

            if score > 0:
                existing_flag = Flag.objects.filter(
                    keyword=keyword,
                    content_item=content
                ).first()

                if existing_flag:
                    # 🔥 SUPPRESSION LOGIC
                    if existing_flag.status == 'irrelevant' and \
                       existing_flag.last_reviewed and \
                       content.last_updated <= existing_flag.last_reviewed:
                        continue

                    # ✅ update only score (DO NOT override status)
                    existing_flag.score = score
                    existing_flag.save()

                else:
                    # ✅ create new flag
                    Flag.objects.create(
                        keyword=keyword,
                        content_item=content,
                        score=score,
                        status='pending'
                    )