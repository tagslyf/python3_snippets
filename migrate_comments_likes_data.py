from reaction.models import (AppComment, AppCommentLike, AppLike, AppReply, AppReplyLike, ArticleComment, ArticleLike,
                             ArticleCommentLike, ArticleReply, ArticleReplyLike, Comment, Like,)


app_comments = Comment.objects.filter(app__isnull=False, is_active=True)
app_likes = Like.objects.filter(app__isnull=False, is_active=True)
article_comments = Comment.objects.filter(article__isnull=False, is_active=True)
article_likes = Like.objects.filter(article__isnull=False, is_active=True)

for app_like in app_likes:
    app_like_data = {
        'app': app_like.app,
        'is_active': app_like.is_active,
        'created_by': app_like.created_by,
        'updated_by': app_like.updated_by,
    }
    app_like_obj = AppLike.objects.create(**app_like_data)
    app_like_obj.created_at = app_like.created_at
    app_like_obj.updated_at = app_like.updated_at
    app_like_obj.save()


for article_like in article_likes:
    article_like_data = {
        'article': article_like.article,
        'is_active': article_like.is_active,
        'created_by': article_like.created_by,
        'updated_by': article_like.updated_by,
    }
    article_like_obj = ArticleLike.objects.create(**article_like_data)
    article_like_obj.created_at = article_like.created_at
    article_like_obj.updated_at = article_like.updated_at
    article_like_obj.save()


for app_comment in app_comments:
    app_comment_data = {
        'app': app_comment.app,
        'comments': app_comment.comments,
        'is_active': app_comment.is_active,
        'created_by': app_comment.created_by,
        'updated_by': app_comment.updated_by,
    }
    app_comment_obj = AppComment.objects.create(**app_comment_data)
    app_comment_obj.created_at = app_comment.created_at
    app_comment_obj.updated_at = app_comment.updated_at
    app_comment_obj.save()
    app_comment_likes = app_comment.comment_likes.filter(is_active=True)
    if app_comment_likes.exists():
        for app_comment_like in app_comment_likes:
            app_comment_like_data = {
                'app_comment': app_comment_obj,
                'is_active': app_comment_like.is_active,
                'created_by': app_comment_like.created_by,
                'updated_by': app_comment_like.updated_by,
            }
            app_comment_like_obj = AppCommentLike.objects.create(**app_comment_like_data)
            app_comment_like_obj.created_at = app_comment_like.created_at
            app_comment_like_obj.updated_at = app_comment_like.updated_at
            app_comment_like_obj.save()
    app_comment_replies = app_comment.comment_replies.filter(is_active=True, reply_to=app_comment)
    if app_comment_replies.exists():
        for app_comment_reply in app_comment_replies:
            app_comment_reply_data = {
                'app_comment': app_comment_obj,
                'comments': app_comment_reply.comments,
                'is_active': app_comment_reply.is_active,
                'created_by': app_comment_reply.created_by,
                'updated_by': app_comment_reply.updated_by,
            }
            app_comment_reply_obj = AppReply.objects.create(**app_comment_reply_data)
            app_comment_reply_obj.created_at = app_comment_reply.created_at
            app_comment_reply_obj.updated_at = app_comment_reply.updated_at
            app_comment_reply_obj.save()
            app_comment_reply_replies = app_comment_reply.replies_to.filter(is_active=True)
            for app_comment_reply_reply in app_comment_reply_replies:
                app_comment_reply_reply_data = {
                    'app_comment': app_comment_obj,
                    'reply_to': app_comment_reply_obj,
                    'comments': app_comment_reply_reply.comments,
                    'is_active': app_comment_reply_reply.is_active,
                    'created_by': app_comment_reply_reply.created_by,
                    'updated_by': app_comment_reply_reply.updated_by,
                }
                app_comment_reply_reply_obj = AppReply.objects.create(**app_comment_reply_reply_data)
                app_comment_reply_reply_obj.created_at = app_comment_reply_reply.created_at
                app_comment_reply_reply_obj.updated_at = app_comment_reply_reply.updated_at
                app_comment_reply_reply_obj.save()
                app_comment_reply_reply_likes = app_comment_reply_reply.comment_likes.filter(is_active=True)
                if app_comment_reply_reply_likes.exists():
                    for app_comment_reply_reply_like in app_comment_reply_reply_likes:
                        app_comment_reply_reply_like_data = {
                            'is_active': app_comment_reply_reply_like.is_active,
                            'app_reply': app_comment_reply_reply_obj,
                            'created_by': app_comment_reply_reply_like.created_by,
                            'updated_by': app_comment_reply_reply_like.updated_by,
                        }
                        app_comment_reply_reply_like_obj = AppReplyLike.objects.create(**app_comment_reply_reply_like_data)
                        app_comment_reply_reply_like_obj.created_at = app_comment_reply_reply_like.created_at
                        app_comment_reply_reply_like_obj.updated_at = app_comment_reply_reply_like.updated_at
                        app_comment_reply_reply_like_obj.save()
            app_comment_reply_likes = app_comment_reply.comment_likes.filter(is_active=True)
            if app_comment_reply_likes.exists():
                for app_comment_reply_like in app_comment_reply_likes:
                    app_comment_reply_like_data = {
                        'is_active': app_comment_reply_like.is_active,
                        'app_reply': app_comment_reply_obj,
                        'created_by': app_comment_reply_like.created_by,
                        'updated_by': app_comment_reply_like.updated_by,
                    }
                    app_comment_reply_like_obj = AppReplyLike.objects.create(**app_comment_reply_like_data)
                    app_comment_reply_like_obj.created_at = app_comment_reply_like.created_at
                    app_comment_reply_like_obj.updated_at = app_comment_reply_like.updated_at
                    app_comment_reply_like_obj.save()


for article_comment in article_comments:
    article_comment_data = {
        'article': article_comment.article,
        'comments': article_comment.comments,
        'is_active': article_comment.is_active,
        'created_by': article_comment.created_by,
        'updated_by': article_comment.updated_by,
    }
    article_comment_obj = ArticleComment.objects.create(**article_comment_data)
    article_comment_obj.created_at = article_comment.created_at
    article_comment_obj.updated_at = article_comment.updated_at
    article_comment_obj.save()
    article_comment_likes = article_comment.comment_likes.filter(is_active=True)
    if article_comment_likes.exists():
        for article_comment_like in article_comment_likes:
            article_comment_like_data = {
                'article_comment': article_comment_obj,
                'is_active': article_comment_like.is_active,
                'created_by': article_comment_like.created_by,
                'updated_by': article_comment_like.updated_by,
            }
            article_comment_like_obj = ArticleCommentLike.objects.create(**article_comment_like_data)
            article_comment_like_obj.created_at = article_comment_like.created_at
            article_comment_like_obj.updated_at = article_comment_like.updated_at
            article_comment_like_obj.save()
    article_comment_replies = article_comment.comment_replies.filter(is_active=True, reply_to=article_comment)
    if article_comment_replies.exists():
        for article_comment_reply in article_comment_replies:
            article_comment_reply_data = {
                'article_comment': article_comment_obj,
                'comments': article_comment_reply.comments,
                'is_active': article_comment_reply.is_active,
                'created_by': article_comment_reply.created_by,
                'updated_by': article_comment_reply.updated_by,
            }
            article_comment_reply_obj = ArticleReply.objects.create(**article_comment_reply_data)
            article_comment_reply_obj.created_at = article_comment_reply.created_at
            article_comment_reply_obj.updated_at = article_comment_reply.updated_at
            article_comment_reply_obj.save()
            article_comment_reply_replies = article_comment_reply.replies_to.filter(is_active=True)
            for article_comment_reply_reply in article_comment_reply_replies:
                article_comment_reply_reply_data = {
                    'article_comment': article_comment_obj,
                    'reply_to': article_comment_reply_obj,
                    'comments': article_comment_reply_reply.comments,
                    'is_active': article_comment_reply_reply.is_active,
                    'created_by': article_comment_reply_reply.created_by,
                    'updated_by': article_comment_reply_reply.updated_by,
                }
                article_comment_reply_reply_obj = ArticleReply.objects.create(**article_comment_reply_reply_data)
                article_comment_reply_reply_obj.created_at = article_comment_reply_reply.created_at
                article_comment_reply_reply_obj.updated_at = article_comment_reply_reply.updated_at
                article_comment_reply_reply_obj.save()
                article_comment_reply_reply_likes = article_comment_reply_reply.comment_likes.filter(is_active=True)
                if article_comment_reply_reply_likes.exists():
                    for article_comment_reply_reply_like in article_comment_reply_reply_likes:
                        article_comment_reply_reply_like_data = {
                            'is_active': article_comment_reply_reply_like.is_active,
                            'article_reply': article_comment_reply_reply_obj,
                            'created_by': article_comment_reply_reply_like.created_by,
                            'updated_by': article_comment_reply_reply_like.updated_by,
                        }
                        article_comment_reply_reply_like_obj = ArticleReplyLike.objects.create(**article_comment_reply_reply_like_data)
                        article_comment_reply_reply_like_obj.created_at = article_comment_reply_reply_like.created_at
                        article_comment_reply_reply_like_obj.updated_at = article_comment_reply_reply_like.updated_at
                        article_comment_reply_reply_like_obj.save()
            article_comment_reply_likes = article_comment_reply.comment_likes.filter(is_active=True)
            if article_comment_reply_likes.exists():
                for article_comment_reply_like in article_comment_reply_likes:
                    article_comment_reply_like_data = {
                        'is_active': article_comment_reply_like.is_active,
                        'article_reply': article_comment_reply_obj,
                        'created_by': article_comment_reply_like.created_by,
                        'updated_by': article_comment_reply_like.updated_by,
                    }
                    article_comment_reply_like_obj = ArticleReplyLike.objects.create(**article_comment_reply_like_data)
                    article_comment_reply_like_obj.created_at = article_comment_reply_like.created_at
                    article_comment_reply_like_obj.updated_at = article_comment_reply_like.updated_at
                    article_comment_reply_like_obj.save()
