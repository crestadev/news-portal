from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets, exceptions

from api.permissions import IsStaffOrOwner
from api.serializers import CategorySerializer, CommentSerializer, ContactSerializer, GroupSerializer, NewsletterSerializer, PostPublishSerializer, PostSerializer, TagSerializer, UserSerializer
from newspaper.models import Category, Comment, Contact, Newsletter, Post, Tag
from django.db.models import Q
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.views import APIView
from rest_framework import status, exceptions
from django.utils import timezone


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]


class GroupViewSet(viewsets.ModelViewSet):

    queryset = Group.objects.all().order_by('name')
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAdminUser]



class TagViewSet(viewsets.ModelViewSet):

    queryset = Tag.objects.all().order_by('name')
    serializer_class = TagSerializer
    permission_classes = [permissions.IsAdminUser]

    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
            return [permissions.AllowAny()]
        
        return super().get_permissions()


class CategoryViewSet(viewsets.ModelViewSet):

    queryset = Category.objects.all().order_by('name')
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAdminUser]

    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
            return [permissions.AllowAny()]
        
        return super().get_permissions()

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('name')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAdminUser]

    def get_queryset(self):
        query_set = super().get_queryset()
        if self.action in ["list", "retrieve"]:
            queryset = queryset.filter(status="active", published_at__isnull=False)

            search_term = self.request.query_params.get("search", None)
            if search_term:

                queryset= queryset.filter(
                    Q(title__icontains=search_term) | Q(content__icontains=search_term)
                )

        return queryset
    
    
    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
            return [permissions.AllowAny()]
        
        return super().get_permissions()
    
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.views_count +=1
        instance.save(update_fields=["views_count"])
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
    
class PostListByCategoryView(ListAPIView):
    queryset = Post.objects.al()
    serializer_class = PostSerializer
    permission_classes = [permissions.AllowAny]


    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(
            status="active",
            published_at__isnull=False,
            category=self.kwargs["category_id"],
        )    
        return queryset
    
class PostListByTagView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.AllowAny]


    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(
            status="active",
            published_at__isnull=False,
            tag=self.kwargs["tag_id"],
        )    
        return queryset
    
class DraftListView(ListAPIView):
    queryset = Post.objects.filter(published_at__isnull=True)
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAdminUser]

class DraftDetailView(RetrieveAPIView):
    queryset = Post.objects.filter(published_at__isnull=True)
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAdminUser]

class PostPublishViewSet(APIView):
    permission_classes = [permissions.IsAdminUser]

    def post(self, request, *args, **kwargs):
        serializer = PostPublishSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            data = serializer.data


            post= Post.objects.get(pk=data["id"])
            post.published_at= timezone.now()
            post.save()

            serialized_data = PostSerializer(post).data
            return Response(serialized_data, status=status.HTTP_200_OK)
        
class CommentListCreateAPIView(APIView):
    permission_classes = [permissions.AllowAny]

    def get_permissions(self):
        if self.request.method =="POST":
            return [permissions.IsAuthenticated()]
        return [permissions.AllowAny()]
    
    def get(self,request, post_id, *args, **kwargs):
        comments = Comment.objects.filter(post=post_id).order_by("-created_at")
        serialized_data = CommentSerializer(comments, many=True).data
        return Response(serialized_data, status=status.HTTP_200_OK)
    
    def post(self, request, post_id, *args, **kwargs):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(post_id=post_id, user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
class CommentDetailAPIView(APIView):
    permission_classes = [IsStaffOrOwner]

    def get_object(self, pk):
        try:
            obj = Comment.objects.get(pk=pk)
            self.check_object_permissions(self.request, obj)
            return obj
        except Comment.DoesNotExist:
            raise exceptions.NotFound({"detail": "Comment not found."})
        
    def get(self, request, post_id, pk, *args, **kwargs):
        comment = self.get_object(pk)
        serialized_data = CommentSerializer(comment).data
        return Response(serialized_data, status=status.HTTP_200_OK)
    
    def put(self, request, post_id, pk, *args, **kwargs):
        comment = self.get_object(pk)
        serializer = CommentSerializer(comment, data=request.data, partial=False)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
    def patch(self, request, post_id, pk, *args, **kwargs):
        comment = self.get_object(pk)
        serializer = CommentSerializer(comment, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
    def delete(self, request, post_id, pk, *args, **kwargs):
        comment = self.get_object(pk)
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class NewsletterViewSet(viewsets.ModelViewSet):
    queryset= Newsletter.objects.all()
    serializer_class = NewsletterSerializer
    permission_classes = [permissions.AllowAny]

    def get_permissions(self):
        if self.action in ["list", "retrieve", "destroy"]:
            return [permissions.IsAdminUser()]
        return super().get_permissions()
    
    def update(self, request, *args, **kwargs):
        raise exceptions.MethodNotAllowed(request.method)
    

class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [permissions.AllowAny]

    def get_permissions(self):
        if self.action in ["list", "retrieve", "destroy"]:
            return [permissions.IsAdminUser()]
        return super().get_permissions()
    
    def update(self, request, *args, **kwargs):
        raise exceptions.MethodNotAllowed(request.method)